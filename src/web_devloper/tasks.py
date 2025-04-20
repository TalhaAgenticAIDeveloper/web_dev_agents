from crewai import  Task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os 
load_dotenv()


os.getenv("GEMINI_API_KEY")




research_tool = SerperDevTool()

class Web_Developer_Tasks():
    ##############################################################################################################
    # Task 1
    ##############################################################################################################

    def Requirement_Analysis_Task(self, agent, project_Title, project_features):
        return Task(
            description=f"""Analyze and refine the raw project requirements for '{project_Title}'. 

            The agent will:
            - Evaluate the given raw requirements: {project_features}
            - Identify missing details or ambiguities
            - Provide a structured technical document outlining the full project scope

            Parameters:
            - Project Title: {project_Title}
            - Project features: {project_features}

            The agent will ensure that the requirements are clear, complete, and technically feasible.
            """,
            tools=[],
            agent=agent,
            expected_output="A well-structured technical document detailing refined project requirements."
        )

    ##############################################################################################################
    # Task 2
    ##############################################################################################################

    def HTML_Generation_Task(self, agent, context):
        return Task(
            description=f"""Generate a clean and semantic HTML structure based on the project requirements.

            The agent will:
            - Translate the analyzed requirements into static HTML layout
            - Use proper HTML5 tags and semantic structuring
            - Include relevant IDs or class placeholders (no styling or scripting)

            The agent must exclude any CSS or JavaScript and focus strictly on the HTML markup.
            """,
            tools=[],
            agent=agent,
            context=context,
            expected_output="Well-structured and complete HTML code for the frontend. nothing except code"
        )
    
    ##############################################################################################################
    # Task 3 - Tailwind Styler
    #############################################################################################################

    def Tailwind_Styling_Task(self, agent, context):
        return Task(
            description=f"""Enhance the raw HTML with Tailwind CSS utility classes to create a modern, responsive UI.

            The agent will:
            - Apply Tailwind classes for layout, spacing, typography, colors, and responsiveness
            - Ensure mobile-first design and accessibility
            - Avoid using any custom CSS or external stylesheets

            The agent must deliver styled HTML with Tailwind utility classes directly embedded.
            """,
            tools=[],
            agent=agent,
            context=context,
            expected_output="Tailwind CSS-styled HTML code ready for rendering in a browser.nothing except code"
        )


    ##############################################################################################################
    # Task 9 - JavaScript Enhancement
    ##############################################################################################################

    def JavaScript_Enhancement_Task(self, agent, context):
        return Task(
            description=f"""Add interactivity to the Tailwind-styled HTML using vanilla JavaScript.

            The agent will:
            - Identify interactive elements such as buttons, forms, toggles, modals, etc.
            - Write clean vanilla JavaScript to enhance user interaction
            - Embed JavaScript at the end of the HTML (inside a <script> tag)

            The agent must avoid using external libraries or frameworks and ensure browser compatibility.
            """,
            tools=[],
            agent=agent,
            context=context,
            expected_output="A single HTML file with embedded JavaScript for frontend interactivity.nothing except code"
        )

    ##################################################################################################
    # Task: GSAP Animation Integration Task
    ##################################################################################################

    def GSAP_Animation_Task(self, agent, context):
        return Task(
            description=f"""Inject GSAP animations into the provided HTML file.

            The agent will:
            - Scan the HTML and identify suitable elements (e.g., hero sections, buttons, cards)
            - Add GSAP CDN link in the head (if not already present)
            - Write JavaScript code using GSAP to animate elements on load, scroll, or hover
            - Embed that JS into a <script> tag at the end of the HTML file

            The returned file must be a complete HTML document with animations working on top of Tailwind CSS and any pre-existing JavaScript.
            """,
            tools=[],
            agent=agent,
            context=context,
            expected_output="A fully updated HTML file with GSAP animations integrated and ready to run in the browser."
        )
