from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = "" ## Add OPEN API Key here.

## User your own custom tool (similar to python function)
def get_company_symbol(company: str)->str:
    """ Use this function to get the symbol for a company

    Args:
        company (str): Name of the company

    Returns:
        str: Symbol of the company
    """
    symbols = {
        "phidata": "AMD",
        "amazon": "AMZN",
        "netflix": "NFLX",
        "nvidia": "NVDA",
        "meta": "META",
        "google": "GOOGL",
        "apple": "AAPL",
        "microsoft": "MSFT",
        "tesla": "TSLA",
        "jpmorgan": "JPM",
        "visa": "V",
        "mastercard": "MA",       
    }

    return symbols.get(company, "Unknown")

## Using the Groq and OpenAI model to see the difference
agent = Agent(
    #model = Groq(id ="llama-3.1-70b-versatile"),
    model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True,stock_fundamentals=True)
             ,get_company_symbol],
    instructions = ["Use tables to display data", 
                    "If you don't know the company symbol, please use get_company_symbol tool, event if it is not a public company"],
    show_tool_calls = True,
    markdown = True,
    debug_mode= True,
)

agent.print_response("Summarize and compare the latest analyst recomendation and fundamentals for NVDA and phidata"
                     ,stream=True)






