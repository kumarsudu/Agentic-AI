from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = "" # Add the Open API Key

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    markdown=True,
)

agent.print_response(
    "Tell me about this image and give me the latest updates about it.",
    images=["https://commons.wikimedia.org/wiki/Main_Page#/media/File:Canterbury_Cathedral_Choir_1,_Kent,_UK_-_Diliff.jpg"],
    stream=True,
)
