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

DEFAULT_TEMPLATE = """You will be writing an extremely effective cover letter for a job candidate applying to a specific role. I will provide you with two key inputs:

<candidate_description>
{{CANDIDATE_DESCRIPTION}}
</candidate_description>

<job_description>
{{JOB_DESCRIPTION}}
</job_description>

Please carefully review the candidate's skills, experience, and qualifications detailed in the candidate description. Then study the job description to understand the role and key requirements.

<brainstorming>
Based on the candidate's background and the job requirements, brainstorm the most compelling points to include in the cover letter. Consider how to best highlight the candidate's relevant skills and experience to position them as a strong fit for this specific role. Jot down your ideas here.
</brainstorming>

Now, write a cover letter tailored for this candidate and job. The cover letter should:

- Grab the reader's attention with a strong opening 
- Demonstrate the candidate's fit by connecting their qualifications to the job requirements
- Provide specific examples of the candidate's relevant experience and accomplishments
- Showcase the candidate's enthusiasm for the role and company
- Close with a confident call-to-action

Remember, the goal is to make a compelling case for this candidate's fit for this particular role. Highlight their most pertinent skills and experience, rather than providing an exhaustive overview. Aim for concise, impactful language.

Please output the full cover letter text inside <cover_letter> tags."""

DEFAULT_CANDIDATE_DESCRIPTION = """# Erik Nomitch: Professional Summary

**Professional Overview:**

Erik Nomitch is a Senior Software Engineer with over a decade of experience specializing in AI, full-stack web development, and systems engineering. Recognized as a pioneer in AI technology, Erik has made significant contributions to early developments in large language models (LLMs), including OpenAI's GPT-3.

**Core Expertise:**

- AI Engineering: Systems integration and advanced prompt engineering.
- LLM Integration: Implementing AI technologies through APIs, web frontends, and autonomous agents.
- System Design: Developing pipelines and systems for real-world AI applications.

**Technical Skills:**

- Programming Languages: Python, JavaScript (ES6+), TypeScript.
- Frameworks & Tools: React, Next.js, Ruby on Rails, Node.js.
- Databases: PostgreSQL, MongoDB.
- DevOps: Docker, Kubernetes, AWS, Google Cloud Platform.
- Other Skills: UI/UX Design, API Development, Cloud Computing, Git, Linux, Bash Scripting.

**Professional Experience:**

- **Chief Technology Officer, StoryMagic.ai (2023 - Present):** Leading technology strategy and development.
- **Software Engineer, MLW AI, Inc. (2018 - 2023):** Focused on machine learning and AI integration.
- **Software Engineer, Hunt Club (2016 - 2018):** Worked on software development and system architecture.
- **Founder, Prelang (2013 - 2016):** Established a startup developing automated programming tools.
- **Co-Founder & Developer, Meta.ai (2010 - 2011):** Early involvement in AI startups, focusing on meta-learning systems.

**Additional Skills and Interests:**

- Comprehensive knowledge in frontend and backend development, database management, and cloud-based architectures.
- Experienced in startup environments, showcasing strong entrepreneurship skills.
- Technical proficiencies include extensive use of Hugging Face Transformers, Jupyter Notebooks, and IoT systems.
- Versatile in both object-oriented and functional programming paradigms, and adept in technical writing and documentation.

Erik Nomitch is a distinguished figure in the tech industry, leveraging extensive technical skills to innovate and drive advancements in AI and software development.
"""

DEFAULT_JOB_DESCRIPTION = """We are looking for a software engineer to join our team. The ideal candidate will have experience with Python, Java, and SQL. They should also have experience working with large datasets and be comfortable working in a fast-paced environment."""

DEFAULT_TEXT_AREA_HEIGHT = 200
   
with st.expander("Prompt Template", expanded=False):
    template_text = st.code(DEFAULT_TEMPLATE.strip(), language="handlebars")

# st.markdown("---")

with st.expander("Create Cover Letter", expanded=st.session_state['rendered_prompt'] == False):
# Create text areas
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Information about you, the candidate")
        st.markdown("""
    Fill this in with as much information about you as you want. This will be used to generate a cover letter for a job application.

    > 💡 Quick tip:
    > As a starting point, go to your LinkedIn profile and copy the "About", "Experience", and "Skills" sections.

    You can also include any other relevant information that you think is important. The more information you provide, the better the generated cover letter will be.

    See [my example](https://eriknomitch.notion.site/Erik-Nomitch-Description-acd07d60c12f4222b06ca43b717f063a) for a full candidate description. _Note that yours does not have to be as detailed._
    """)
        candidate_description = st.text_area("Candidate Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_CANDIDATE_DESCRIPTION.strip())

        st.markdown("""---""")

        # with col2:
        st.subheader("Information about the job you're applying for")
        st.markdown("""
Go to the job posting, copy the _full_ job description, and paste it here. You can also include any other relevant information that you think is important.
    """)
        job_description = st.text_area("Job Description", height=DEFAULT_TEXT_AREA_HEIGHT, value=DEFAULT_JOB_DESCRIPTION.strip())



def render_template(template_text, job_description, candidate_description):
    if template_text and job_description and candidate_description:
        template = Template(DEFAULT_TEMPLATE)
        rendered_text = template.render(JOB_DESCRIPTION=job_description, CANDIDATE_DESCRIPTION=candidate_description)
        print(rendered_text)
        st.session_state['rendered_prompt'] = rendered_text
    else:
        st.warning("Please fill in all the fields")

# Create a button
button_clicked = st.button("Render Full Prompt", key="render_button", help="Click this button to render the full prompt")

if button_clicked:
    render_template(template_text, job_description, candidate_description)

if st.session_state['rendered_prompt'] != False and st.session_state['rendered_prompt'] != "":
    st.success("Prompt rendered successfully")
    st.markdown("""
# Full Prompt
Use the following prompt to generate your cover letter:
    """)
    st.code(st.session_state['rendered_prompt'], language="handlebars")

