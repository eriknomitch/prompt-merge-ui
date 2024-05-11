import streamlit as st
from jinja2 import Template

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
   
with st.expander("Template", expanded=True):
    template_text = st.code(DEFAULT_TEMPLATE, language="handlebars")

# Create text areas
col1, col2 = st.columns(2)
with col1:
    candidate_description = st.text_area("Candidate Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_CANDIDATE_DESCRIPTION)
with col2:
    job_description = st.text_area("Job Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_JOB_DESCRIPTION)

# Create a button
button_clicked = st.button("Render")

# Create an output area
output_area = st.empty()

def render_template(template_text, job_description, candidate_description):
    if template_text and job_description and candidate_description:
        template = Template(template_text)
        rendered_text = template.render(JOB_DESCRIPTION=job_description, CANDIDATE_DESCRIPTION=candidate_description)
        print(rendered_text)
        output_area.text_area("Rendered Output:", value=rendered_text, height=100)
    else:
        st.warning("Please fill in all the fields")

if button_clicked:
    render_template(template_text, job_description, candidate_description)

