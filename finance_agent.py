from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools


# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",              # Gives the agent an identifier name
    role="You are a helpful assistant.You can search the web for information.", # Defines the agent's behavior/persona
    model=Groq(                           # Specifies the AI model to use
        id="llama3-groq-70b-8192-tool-use-preview"  # Specific model identifier
    ),
    tools=[DuckDuckGo()],                # Array of tools - here just DuckDuckGo search
    instructions=["Always include sources"], # Additional behavior instructions
    show_tool_calls=True,                # Makes tool usage visible/transparent
    markdown=True,                        # Enables markdown formatting in responses
    verbose=True,                         # Enables detailed logging/output
)

## Financial Agent
finance_agent = Agent(
    name="Finance Agent",
    role="You are a helpful assistant. You can search the web for information and get stock prices.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    #model = OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_agent = Agent(
    team = [web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions = ["Always include sources","Use tables to display data"],
    show_tool_calls = True,
    markdown = True,
)

multi_agent.print_response("Provide your recommendation for the stock MSFT best price to buy based on the latest news and analyst recommendations.",stream=True)