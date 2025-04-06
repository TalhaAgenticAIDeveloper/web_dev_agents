from agents import Web_Developer_Agents
from tasks import Web_Developer_Tasks
from crewai import Crew, Process, LLM
import litellm
import streamlit as st
import markdown
from dotenv import load_dotenv
from io import StringIO
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

st.title("🛠️ AI Project Management Assistant")

############################################################################################
# Taking Inputs
############################################################################################

project_Title = st.text_input("Project Title")
project_features = st.text_area("Enter Project features")


############################################################################################
# Creating Agents and Tasks
############################################################################################

agents = Web_Developer_Agents()
tasks = Web_Developer_Tasks()

# Importing Agents
Requirement_Analysis_Agent = agents.Requirement_Analysis_Agent()
HTML_Generator_Agent = agents.HTML_Generator_Agent()
Tailwind_Styler_Agent = agents.Tailwind_Styler_Agent()
JavaScript_Enhancer_Agent = agents.JavaScript_Enhancer_Agent()



# Assigning Tasks

# Task 1
Requirement_Analysis_Task = tasks.Requirement_Analysis_Task(
    agent=Requirement_Analysis_Agent,
    project_Title=project_Title,
    project_features=project_features,

)

# Task 2
HTML_Generation_Task = tasks.HTML_Generation_Task(
    
    agent = HTML_Generator_Agent,

    context = [Requirement_Analysis_Task],
)

# Task 3
Tailwind_Styling_Task = tasks.Tailwind_Styling_Task(
    agent = Tailwind_Styler_Agent,
    context = [HTML_Generation_Task],
)



# Task 4
JavaScript_Enhancement_Task = tasks.JavaScript_Enhancement_Task(
    agent=JavaScript_Enhancer_Agent,
    context=[Tailwind_Styling_Task]
)



############################################################################################
# Creating Crew
############################################################################################

crew = Crew(
    agents=[Requirement_Analysis_Agent, HTML_Generator_Agent,Tailwind_Styler_Agent,JavaScript_Enhancer_Agent],
    tasks=[Requirement_Analysis_Task,HTML_Generation_Task,Tailwind_Styling_Task,JavaScript_Enhancement_Task],
    verbose=True,
)

def save_output_to_markdown(output, filename="website_code.txt"):
    """Saves the output in a structured text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output.replace("**", ""))

if st.button("Generate Report"):
    with st.spinner("Processing... Please wait"):
        results = crew.kickoff()
        output_text = results.raw if hasattr(results, 'raw') else str(results)
        st.markdown(output_text)
        output_buffer = StringIO()
        output_buffer.write(output_text)
        st.download_button(
            label="Download Report",
            data=output_buffer.getvalue(),
            file_name="project_report.md",
            mime="text/markdown"
        )
