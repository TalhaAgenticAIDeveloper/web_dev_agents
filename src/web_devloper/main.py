from agents import Web_Developer_Agents
from tasks import Web_Developer_Tasks
from crewai import Crew, Process, LLM
import litellm
import streamlit as st
import markdown
from dotenv import load_dotenv
from io import StringIO
import os
# from litellm import Completion

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

llm1 = LLM(
    model = "gemini/gemini-2.0-flash-exp",
    api_key = api_key
)

if not api_key:
    st.error("⚠️ GEMINI_API_KEY not found. Please check your .env file.")
    st.stop()

st.title("🛠️ AI Website builder")

############################################################################################
# Taking Inputs
############################################################################################

project_Title = st.text_input("Project Title")
# project_features = st.text_area("Enter Project features")






def create_prompt_for_single_page_features(project_title):
    prompt = f"""
        You are an AI assistant specialized in designing **single-page websites**. Your task is to analyze the given project title and suggest only the **most essential features** that such a page might require, in the form of **clear yes/no questions**.

        ### **Instructions:**
        - ONLY focus on **single-page websites**.
        - Based on the project title, suggest **5 to 6 important sections or components** that are typically needed on a single-page site.
        - **Do not include any extra words, introductions, explanations, or formatting.**
        - Your output should be **ONLY the list of feature-related questions**, nothing else.
        - Each question must begin with one of the following:
          - "Do you want to add..."
          - "Would you like to include..."
          - "Should the page have..."
          - "Do you need a section for..."
          - "Would it be helpful to add..."

        ### **Project Title:** {project_title}
    """
    return prompt





def get_litellm_response(prompt):
    response = litellm.completion(
        model="gemini/gemini-2.0-flash-exp",  
        api_key=api_key,
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Session State Handling
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}

if st.button("Take Interview"):
    if project_Title:
        question_prompt = create_prompt_for_single_page_features(project_Title)
        questions_response = get_litellm_response(question_prompt)
        st.session_state.chat_history = [q.strip() for q in questions_response.split("\n") if q.strip()]
        st.session_state.current_question = 0

    # Store questions and answers in a structured dictionary
if "qa_pairs" not in st.session_state:
        st.session_state.qa_pairs = {}

    # Display Questions
if st.session_state.chat_history:
        index = st.session_state.current_question
        if index < len(st.session_state.chat_history):  
            question = st.session_state.chat_history[index]
            st.subheader(f"🤖 Question {index+1}: {question}")
            user_answer = st.text_input("✏️ Your Answer", key=f"answer_{index}")

            if st.button("Next"):
                if user_answer.strip():
                    # Store question and answer together
                    st.session_state.qa_pairs[question] = user_answer
                    st.session_state.current_question += 1
                    st.rerun()
                else:
                    st.warning("⚠️ Please enter an answer before proceeding.")






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
GSAP_Animator_Agent = agents.GSAP_Animator_Agent()
manager = agents.manager()


# Assigning Tasks

# Task 1
Requirement_Analysis_Task = tasks.Requirement_Analysis_Task(
    agent=Requirement_Analysis_Agent,
    project_Title=project_Title,
    project_features=st.session_state.qa_pairs,

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


# Task 4
GSAP_Animation_Task = tasks.GSAP_Animation_Task(
    agent=GSAP_Animator_Agent,
    context=[JavaScript_Enhancement_Task]
)
 

############################################################################################
# Creating Crew
############################################################################################

crew = Crew(
    agents=[Requirement_Analysis_Agent, HTML_Generator_Agent,Tailwind_Styler_Agent,JavaScript_Enhancer_Agent],
    tasks=[Requirement_Analysis_Task,HTML_Generation_Task,Tailwind_Styling_Task,JavaScript_Enhancement_Task],
    # manager_agent=manager,
    # function_calling_llm=llm1,
    # process = Process.hierarchical,
    verbose=True,
)

def save_output_to_markdown(output, filename="website_code.html"):
    """Saves the output in a structured text file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output.replace("**", ""))

if st.button("Generate code"):
    with st.spinner("Processing... Please wait"):
        results = crew.kickoff()
        output_text = results.raw if hasattr(results, 'raw') else str(results)
        st.markdown(output_text)
        output_buffer = StringIO()
        output_buffer.write(output_text)
        st.download_button(
            label="Download Report",
            data=output_buffer.getvalue(),
            file_name="project_report.html",
            mime="text/markdown"
        )
