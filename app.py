import streamlit as st
from jinja2 import Template

st.set_page_config(layout="wide")

if 'initialized' not in st.session_state:
    st.session_state['initialized'] = True

if 'rendered_prompt' not in st.session_state:
    st.session_state['rendered_prompt'] = False

with st.sidebar:
    st.header("Cover Letter Generator")
    st.write("Fill in the fields below to generate a cover letter")
    # Add any sidebar widgets here

with st.popover("Open popover"):
    st.markdown("Hello World 👋")
    name = st.text_input("What's your name?")


st.title("Cover Letter Generator")

DEFAULT_TEMPLATE = """<job_description>
{{ JOB_DESCRIPTION }}
</job_description>

<candidate_description>
{{ CANDIDATE_DESCRIPTION }}
</candidate_description>="""

DEFAULT_CANDIDATE_DESCRIPTION = """I am a highly motivated individual with a passion for technology. I have a strong background in software engineering and I am excited about the opportunity to work at your company."""

DEFAULT_JOB_DESCRIPTION = """We are looking for a software engineer to join our team. The ideal candidate will have experience with Python, Java, and SQL. They should also have experience working with large datasets and be comfortable working in a fast-paced environment."""

DEFAULT_TEXT_AREA_HEIGHT = 500
   
with st.expander("Prompt Template", expanded=False):
    template_text = st.code(DEFAULT_TEMPLATE, language="handlebars")

# st.markdown("---")

with st.expander("Create Cover Letter", expanded=True):
# Create text areas
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information about you")
        st.markdown("""
    Fill this in with as much information about you as you want. This will be used to generate a cover letter for a job application.

    As a starting point, go to your LinkedIn profile and copy the "About", "Experience", and "Skills" sections. You can also include any other relevant information that you think is important.

    See [my example](https://eriknomitch.notion.site/Erik-Nomitch-Description-acd07d60c12f4222b06ca43b717f063a) for a full candidate description. _Note that yours does not have to be as detailed._
    """)
        candidate_description = st.text_area("Candidate Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_CANDIDATE_DESCRIPTION)

        # with col2:
        st.subheader("Job Description")
        st.write("Fill in the fields below to generate a cover letter")
        job_description = st.text_area("Job Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_JOB_DESCRIPTION)

# Create an output area
output_area = st.empty()

def render_template(template_text, job_description, candidate_description):
    if template_text and job_description and candidate_description:
        template = Template(DEFAULT_TEMPLATE)
        rendered_text = template.render(JOB_DESCRIPTION=job_description, CANDIDATE_DESCRIPTION=candidate_description)
        print(rendered_text)
        output_area.code(rendered_text, language="handlebars")
        st.session_state['rendered_prompt'] = True
    else:
        st.warning("Please fill in all the fields")

# Create a button
button_clicked = st.button("Render Full Prompt", key="render_button", help="Click this button to render the full prompt")

if button_clicked:
    render_template(template_text, job_description, candidate_description)

