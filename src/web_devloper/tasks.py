from crewai import  Task
# from crewai_tools import SerperDevTool
from crewai.tools import (
    ApifyActorsTool, BrowserbaseLoadTool, CodeDocsSearchTool, CodeInterpreterTool,
    ComposioTool, CSVSearchTool, DALL_E_Tool, DirectorySearchTool, DOCXSearchTool,
    DirectoryReadTool, EXASearchTool, FileReadTool, FirecrawlSearchTool, FirecrawlCrawlWebsiteTool,
    FirecrawlScrapeWebsiteTool, GithubSearchTool, SerperDevTool, TXTSearchTool, JSONSearchTool,
    LlamaIndexTool, MDXSearchTool, PDFSearchTool, PGSearchTool, VisionTool, RagTool,
    ScrapeElementFromWebsiteTool, ScrapeWebsiteTool, WebsiteSearchTool, XMLSearchTool,
    YoutubeChannelSearchTool, YoutubeVideoSearchTool, DecisionSupportTool
)
from crewai import Tool
from dotenv import load_dotenv
import os 
load_dotenv()


os.getenv("GEMINI_API_KEY")

from crewai import Tool

# Tools Import
from tools.docx_search import DocxSearchTool
from tools.research import ResearchTool
from tools.decision_support import DecisionSupportTool
from tools.design import DesignTool
from tools.prototyping import PrototypingTool
from tools.coding import CodingTool
from tools.security import SecurityTool
from tools.database import DatabaseTool
from tools.frontend_testing import FrontendTestingTool
from tools.data_security import DataSecurityTool
from tools.api_documentation import APIDocumentationTool
from tools.testing import TestingTool
from tools.security_testing import SecurityTestingTool
from tools.performance_testing import PerformanceTestingTool

# Initialize Tools
docx_search_tool = DocxSearchTool()
research_tool = ResearchTool()
decision_support_tool = DecisionSupportTool()
design_tool = DesignTool()
prototyping_tool = PrototypingTool()
coding_tool = CodingTool()
security_tool = SecurityTool()
database_tool = DatabaseTool()
frontend_testing_tool = FrontendTestingTool()
data_security_tool = DataSecurityTool()
api_documentation_tool = APIDocumentationTool()
testing_tool = TestingTool()
security_testing_tool = SecurityTestingTool()
performance_testing_tool = PerformanceTestingTool()


research_tool = SerperDevTool()

class Web_Developer_Tasks():
    ##############################################################################################################
    # Task 1
    ##############################################################################################################

    def Requirement_Analysis_Task(self, agent, project_Title, raw_requirements):
        return Task(
            description=f"""Analyze and refine the raw project requirements for '{project_Title}'. 

            The agent will:
            - Evaluate the given raw requirements: {raw_requirements}
            - Identify missing details or ambiguities
            - Provide a structured technical document outlining the full project scope

            Parameters:
            - Project Title: {project_Title}
            - Raw Requirements: {raw_requirements}

            The agent will ensure that the requirements are clear, complete, and technically feasible.
            """,
            tools=[docx_search_tool],
            agent=agent,
            expected_output="A well-structured technical document detailing refined project requirements."
        )

    ##############################################################################################################
    # Task 2
    ##############################################################################################################

    def Tech_Stack_Selection_Task(self, agent, refined_requirements):
        return Task(
            description=f"""Select the optimal technology stack based on the refined project requirements.

            The agent will:
            - Analyze the project scope and functional needs
            - Identify suitable frontend, backend, database, and deployment technologies
            - Justify the technology choices based on scalability, security, and performance

            Parameters:
            - Refined Requirements: {refined_requirements}

            The agent will ensure that the selected stack aligns with the project's goals and best industry practices.
            """,
            tools=[research_tool, decision_support_tool],
            agent=agent,
            expected_output="A detailed report specifying the chosen tech stack with justifications."
        )

    ##############################################################################################################
    # Task 3
    ##############################################################################################################

    def UI_UX_Design_Task(self, agent, refined_requirements):
        return Task(
            description=f"""Develop wireframes and UI/UX design guidelines based on project requirements.

            The agent will:
            - Create wireframes for the key interfaces
            - Define design principles for user experience, accessibility, and responsiveness
            - Provide color schemes, typography, and layout recommendations

            Parameters:
            - Refined Requirements: {refined_requirements}

            The agent will deliver a user-friendly and aesthetically pleasing design plan.
            """,
            tools=[design_tool, prototyping_tool],
            agent=agent,
            expected_output="A set of wireframes and a UI/UX guideline document."
        )

    ##############################################################################################################
    # Task 4
    ##############################################################################################################

    def Backend_Development_Task(self, agent, tech_stack, refined_requirements):
        return Task(
            description=f"""Develop the backend architecture based on the selected technology stack.

            The agent will:
            - Design the API structure and database schema
            - Implement authentication, authorization, and security measures
            - Ensure scalability and efficient data management

            Parameters:
            - Tech Stack: {tech_stack}
            - Refined Requirements: {refined_requirements}

            The agent will build a secure and high-performance backend system.
            """,
            tools=[coding_tool, security_tool, database_tool],
            agent=agent,
            expected_output="A fully functional backend API with database integration."
        )

    ##############################################################################################################
    # Task 5
    ##############################################################################################################

    def Frontend_Development_Task(self, agent, tech_stack, ui_ux_design):
        return Task(
            description=f"""Implement the frontend based on the UI/UX design and selected technology stack.

            The agent will:
            - Convert wireframes into interactive user interfaces
            - Ensure mobile responsiveness and accessibility compliance
            - Integrate frontend with backend APIs for dynamic content

            Parameters:
            - Tech Stack: {tech_stack}
            - UI/UX Design: {ui_ux_design}

            The agent will deliver a polished and fully functional frontend.
            """,
            tools=[coding_tool, frontend_testing_tool],
            agent=agent,
            expected_output="A fully developed frontend integrated with the backend."
        )

    ##############################################################################################################
    # Task 6
    ##############################################################################################################

    def Database_Management_Task(self, agent, tech_stack, refined_requirements):
        return Task(
            description=f"""Design and configure the database architecture for the project.

            The agent will:
            - Select an appropriate database type (SQL/NoSQL) based on project needs
            - Design an optimized schema for fast querying and scalability
            - Implement data security measures like encryption and backups

            Parameters:
            - Tech Stack: {tech_stack}
            - Refined Requirements: {refined_requirements}

            The agent will ensure an efficient and secure database implementation.
            """,
            tools=[database_tool, data_security_tool],
            agent=agent,
            expected_output="A fully optimized and secure database structure."
        )

    ##############################################################################################################
    # Task 7
    ##############################################################################################################

    def API_Development_Task(self, agent, backend_architecture):
        return Task(
            description=f"""Develop and document RESTful or GraphQL APIs for frontend-backend communication.

            The agent will:
            - Implement secure, efficient, and scalable API endpoints
            - Ensure proper authentication and role-based access control
            - Provide API documentation for easy integration

            Parameters:
            - Backend Architecture: {backend_architecture}

            The agent will deliver a well-documented and functional API service.
            """,
            tools=[coding_tool, api_documentation_tool],
            agent=agent,
            expected_output="A fully developed API with complete documentation."
        )

    ##############################################################################################################
    # Task 8
    ##############################################################################################################

    def Testing_Debugging_Task(self, agent, frontend, backend, api_services):
        return Task(
            description=f"""Conduct comprehensive testing of frontend, backend, and APIs.

            The agent will:
            - Perform unit testing, integration testing, and end-to-end testing
            - Identify and document bugs and performance bottlenecks
            - Suggest improvements to enhance stability and security

            Parameters:
            - Frontend: {frontend}
            - Backend: {backend}
            - API Services: {api_services}

            The agent will ensure a bug-free and optimized application.
            """,
            tools=[testing_tool, security_testing_tool, performance_testing_tool],
            agent=agent,
            expected_output="A detailed test report highlighting bugs, fixes, and performance insights."
        )

