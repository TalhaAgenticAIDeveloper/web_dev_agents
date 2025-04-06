from crewai import  Task
from crewai_tools import SerperDevTool
# from crewai.tools import (
#      BrowserbaseLoadTool, CodeDocsSearchTool, CodeInterpreterTool,
#     ComposioTool, CSVSearchTool, DALL_E_Tool, DirectorySearchTool, DOCXSearchTool,
#     DirectoryReadTool, EXASearchTool, FileReadTool, FirecrawlSearchTool, FirecrawlCrawlWebsiteTool,
#     FirecrawlScrapeWebsiteTool, GithubSearchTool, SerperDevTool, TXTSearchTool, JSONSearchTool,
#     LlamaIndexTool, MDXSearchTool, PDFSearchTool, PGSearchTool, VisionTool, RagTool,
#     ScrapeElementFromWebsiteTool, ScrapeWebsiteTool, WebsiteSearchTool, XMLSearchTool,
#     YoutubeChannelSearchTool, YoutubeVideoSearchTool, DecisionSupportTool
# )
# from crewai import Tool
from dotenv import load_dotenv
import os 
load_dotenv()


os.getenv("GEMINI_API_KEY")

# from crewai import Tool

# Tools Import
# from crewai_tools import DocxSearchTool
# from crewai_tools import ResearchTool
# from crewai_tools import DecisionSupportTool
# from crewai_tools import DesignTool
# from crewai_tools import PrototypingTool
# from crewai_tools import CodingTool
# from crewai_tools import SecurityTool
# from crewai_tools import DatabaseTool
# from crewai_tools import FrontendTestingTool
# from crewai_tools import DataSecurityTool
# from crewai_tools import APIDocumentationTool
# from crewai_tools import TestingTool
# from crewai_tools import SecurityTestingTool
# from crewai_tools import PerformanceTestingTool

# # Initialize Tools
# docx_search_tool = DocxSearchTool()
# research_tool = ResearchTool()
# decision_support_tool = DecisionSupportTool()
# design_tool = DesignTool()
# prototyping_tool = PrototypingTool()
# coding_tool = CodingTool()
# security_tool = SecurityTool()
# database_tool = DatabaseTool()
# frontend_testing_tool = FrontendTestingTool()
# data_security_tool = DataSecurityTool()
# api_documentation_tool = APIDocumentationTool()
# testing_tool = TestingTool()
# security_testing_tool = SecurityTestingTool()
# performance_testing_tool = PerformanceTestingTool()


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
            expected_output="Well-structured and complete HTML code for the frontend."
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
            expected_output="Tailwind CSS-styled HTML code ready for rendering in a browser."
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
            expected_output="A single HTML file with embedded JavaScript for frontend interactivity."
        )

