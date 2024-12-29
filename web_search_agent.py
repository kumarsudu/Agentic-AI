from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent = Agent(
    name="Web Search Agent",
    role="You are a helpful assistant. You can search the web for information.",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls = True,
    markdown = True,
    verbose=True,
)

web_search_agent.print_response("What is the weather in New York?",stream=True)