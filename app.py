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

DEFAULT_TEMPLATE = """
You will be writing a cover letter for a job candidate applying to a specific role. I will provide you with two key inputs:

<candidate_description>
{{CANDIDATE_DESCRIPTION}}
</candidate_description>

<job_description>
{{JOB_DESCRIPTION}}
</job_description>

Please carefully review the candidate's skills, experience, and qualifications detailed in the candidate description. Then study the job description to understand the role and key requirements. Based on the job description, deduce the likely audience who will be reading this cover letter. Consider factors like the company culture, seniority of the role, and any other relevant context clues. Tailor the style, tone, and content of the letter to be maximally effective for this particular audience.

<rules>
- IMPORTANT: Only mention skills, experiences, and accomplishments that are explicitly stated in the candidate description. Do not infer or extrapolate qualifications based on the job description or other contextual clues. If the candidate description does not directly say the candidate possesses a certain skill or experience, do not claim that they do.
- Avoid using cliché or stereotypical cover letter phrases. Aim for an authentic, original voice. 
- Be as concise as possible. Focus on making a strong impression efficiently, without unnecessary filler or fluff.
- Strike a balanced tone. Convey the candidate's enthusiasm for the role but avoid coming across as ingratiating or overly effusive.
</rules>

<guidelines>
</guidelines>

<brainstorming>
Based on the candidate's background, the job requirements, and your deduced target audience, brainstorm the most compelling points to include in the cover letter. Consider how to best highlight the candidate's relevant skills and experience to position them as a strong fit for this specific role in a way that will resonate with the audience. Jot down your ideas here.
</brainstorming>

Now, write a cover letter tailored for this candidate, job, and deduced audience. Adhere to the <rules> and guidelines provided above. The cover letter should:

- Grab the reader's attention with a strong opening that will appeal to this audience
- Demonstrate the candidate's fit by connecting their qualifications to the job requirements 
- Provide specific examples of the candidate's relevant experience and accomplishments
- Showcase the candidate's enthusiasm for the role and company in a way that feels authentic to the audience without being overly effusive
- Close with a confident call-to-action that aligns with the audience's likely preferences

Remember, the goal is to make a compelling case for this candidate's fit for this particular role in a way that feels relevant and persuasive to the specific audience you deduced from the job description. Highlight their most pertinent skills and experience, rather than providing an exhaustive overview. Aim for concise, impactful language that will connect with the reader.

Please output the full cover letter text inside <cover_letter> tags.

After you have written the cover letter, please provide a brief explanation of your approach. Discuss how you tailored the content and style for the deduced audience and how you aimed to make a compelling case for the candidate. Put this inside <approach> tags.

Next, review your cover letter and suggest improvements here. Consider aspects like:
- Is the opening attention-grabbing and relevant to the audience? 
- Are the candidate's qualifications clearly connected to the job requirements?
- Are the examples of experience and accomplishments specific and impactful?
- Does the enthusiasm feel authentic and appropriate for the audience?
- Is the call-to-action confident and aligned with audience preferences?
- Is the language concise and compelling overall?
Suggest any changes that could make the cover letter even stronger. Put this inside <review> tags.

Next, implement any changes you feel would improve the cover letter based on your review. Once you are satisfied with your final draft, submit the cover letter text inside <final_cover_letter> tags.

Finally, provide a brief reflection on your process and the final cover letter here. What were the key factors you considered in tailoring your approach? What do you feel are the strongest elements of the final cover letter? Are there any potential weaknesses or areas of uncertainty? Share any final thoughts on the process and product. Put this inside <reflection> tags.


"""

# DEFAULT_TEMPLATE = """You will be writing an extremely effective cover letter for a job candidate applying to a specific role. I will provide you with two key inputs:
#
# <candidate_description>
# {{CANDIDATE_DESCRIPTION}}
# </candidate_description>
#
# <job_description>
# {{JOB_DESCRIPTION}}
# </job_description>
#
# Please carefully review the candidate's skills, experience, and qualifications detailed in the candidate description. Then study the job description to understand the role and key requirements. Finally, consider the audience who will be reading this cover letter, as described in the audience section. Tailor the style, tone, and content of the letter to be maximally effective for this particular audience.
#
# <brainstorming>
# Based on the candidate's background, the job requirements, and the target audience, brainstorm the most compelling points to include in the cover letter. Consider how to best highlight the candidate's relevant skills and experience to position them as a strong fit for this specific role in a way that will resonate with the audience. Jot down your ideas here.
# </brainstorming>
#
# Now, write a cover letter tailored for this candidate, job, and audience. The cover letter should:
#
# - Grab the reader's attention with a strong opening that will appeal to this audience
# - Demonstrate the candidate's fit by connecting their qualifications to the job requirements 
# - Provide specific examples of the candidate's relevant experience and accomplishments
# - Showcase the candidate's enthusiasm for the role and company in a way that feels authentic to the audience
# - Close with a confident call-to-action that aligns with the audience's likely preferences
#
# Remember, the goal is to make a compelling case for this candidate's fit for this particular role in a way that feels relevant and persuasive to the specific audience. Highlight their most pertinent skills and experience, rather than providing an exhaustive overview. Aim for concise, impactful language that will connect with the reader.
#
# Please output the full cover letter text inside <cover_letter> tags.
#
# After you have written the cover letter, please provide a brief explanation of your approach inside <approach> tags.
#
# Next, review your cover letter and suggest improvements inside <review> tags.
#
# Implement any changes you feel are necessary to make the cover letter as strong as possible. Once you are satisfied with your final draft, submit the cover letter text inside <final_cover_letter> tags.
#
# Finally, provide a brief reflection on your process and the final cover letter inside <reflection> tags.
# """


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

DEFAULT_JOB_DESCRIPTION = """# **Software Engineer, Edge**

[Stripe](https://www.linkedin.com/company/stripe/life) · United States

## About the job

Who we are

**About Stripe**

Stripe is a financial infrastructure platform for businesses. Millions of companies - from the world’s largest enterprises to the most ambitious startups - use Stripe to accept payments, grow their revenue, and accelerate new business opportunities. Our mission is to increase the GDP of the internet, and we have a staggering amount of work ahead. That means you have an unprecedented opportunity to put the global economy within everyone's reach while doing the most important work of your career.

**About The Team**

Build the infrastructure powering economic growth.

Stripe’s infrastructure powers businesses all over the world. We process payments, run marketplaces, detect fraud, help entrepreneurs start an internet business from anywhere in the world, build world-class developer-friendly APIs, and more. If you’re an infrastructure engineer here, you’ll get to build distributed systems that are extremely reliable and scale-out horizontally on the cloud. At Stripe we care a very great deal about reliability as our users’ businesses depend on it.

You’ll be on a team that provides a secure, compliant, fast, and reliable infrastructure that connects Stripe’s products to users globally. The Edge team abstracts the underlying complexity of the Internet from our users and own tier-0 mission critical systems like Global Ingress, CDNs (and static assets), DNS and Certificates which power all of Stripe products (Payments, Elements, Connect, Terminal, Radar, Stripe Tax, Usage Billing, and other SaaS and BaaS - Banking as a Service offerings etc.). We power Stripe Frontend, which is used by all Stripe services to allow access from users of the internet. Edge drives Stripe wide initiatives like Multi-region support, Disaster recovery, Data locality, End-to-end (E2E) p50/p95/p99 payment latency, and is on the fore-front of enabling any new business or product line for Stripe. The current stack is built (but not limited to) leveraging AWS Infrastructure, AWS EC2, S3, AWS Elasticache, Auto scaling, AWS Shield, WAF, Distributed services built in GoLang, Load balancers in GoLand, C/C++, Nginx, Tooling in Python, React, JS, and memcached.

The Edge team is part of the High Assurance Engineering organization. The High Assurance Engineering organization is part of the Core Infrastructure organization.

What you’ll do

As a Software Engineer on the Edge team, you will play a pivotal role in optimizing and enhancing the performance, reliability and security of our global Edge infrastructure and collaborate with product teams to design and deliver micro-services which support business needs. You will work at the intersection of cutting-edge technology and real-world impact, collaborating with talented engineers to tackle complex challenges in distributed systems, and networking. You will also build a great customer experience for internal Stripe product teams that rely on the Edge infrastructure to deliver traffic to their services globally and at scale.

**Responsibilities**

- Lead efforts to optimize and enhance the company's edge computing infrastructure, ensuring low-latency, high-performance delivery of payment services to users worldwide through fine-tuning caching strategies, load balancing, and content delivery networks (CDNs) to improve response times and minimize latency.
- Collaborate with cross-functional teams to scale the company's infrastructure in response to growing demand and evolving business requirements by designing and implementing scalable architectures that can handle spikes in traffic during peak periods, while maintaining high availability and fault tolerance.
- Lead incident response efforts during security incidents or service disruptions, working closely with internal teams and external partners to investigate and resolve issues in a timely manner and conducting post-mortem analyses to identify root causes and implementing preventive measures to mitigate future risks.
- Contribute to the design and implementation of robust security architectures for the company's payment systems, incorporating best practices in encryption, access control, and data integrity to protect sensitive customer information and financial transactions.
- Provide technical leadership and mentorship to junior engineers, helping them develop their skills and expertise in edge computing and high-scale tier-0 mission critical distributed systems.
- Conduct code reviews, sharing best practices, and fostering a culture of continuous learning and improvement within the team.

Projects you could work on

- Building infrastructure support millions of requests per second at blazing fast performance with least cost spent on infrastructure
- Achieving 51/2 9s of availability (which means less than 3 mins of downtime in a year!)
- Support large Synchronous and asynchronous event streaming at the Edge
- Supporting the most demanding and high customer impacting Stripe products requiring sub-millisecond latency goals
- Creating a fast and secure platform which is PCI compliant along with reliability SLOs on which critical product teams within Stripe (Payment, Connect, Accounts, Elements, Terminal, and so on..) can have critical dependency on!

Who you are

We're looking for someone who meets the minimum requirements to be considered for the role. If you meet these requirements, you are encouraged to apply. The preferred qualifications are a bonus, not a requirement.

**Minimum Requirements**

- 5+ years of professional experience in a software development role
- A strong engineering background in building distributed systems at scale, with high reliability
- Experience with operational excellence and a deep understanding of metrics, alarms and dashboard
- Experience developing, maintaining and debugging distributed systems
- Experience using or development of distributed systems in one of the major cloud providers

**Preferred Qualifications**

- Ability to write high quality code (in programming languages like Go, Java, C/C++ etc)
- Experience in edge computing (ingress, CDNs) and/or networking
- Experience in Unix shell

It’s not expected that any single candidate would have expertise across all of these areas. For instance, we have wonderful team members who are really focused on their customers’ needs and building amazing user experiences, but didn’t come in with as much systems knowledge.

Hybrid work at Stripe

This role is available either in an office or a remote location (typically, 35+ miles or 56+ km from a Stripe office).

Office-assigned Stripes spend at least 50% of the time in a given month in their local office or with users. This hits a balance between bringing people together for in-person collaboration and learning from each other, while supporting flexibility about how to do this in a way that makes sense for individuals and their teams.

A remote location, in most cases, is defined as being 35 miles (56 kilometers) or more from one of our offices. While you would be welcome to come into the office for team/business meetings, on-sites, meet-ups, and events, our expectation is you would regularly work from home rather than a Stripe office. Stripe does not cover the cost of relocating to a remote location. We encourage you to apply for roles that match the location where you currently or plan to live."""

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

