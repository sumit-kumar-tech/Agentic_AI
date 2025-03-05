from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()


## Web Search Agent
web_search_agent = Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[DuckDuckGo()],
    instructions=["Always inclue sources"],
    show_tool_calls=True,
    markdown=True

)

## Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="mixtral-8x7b-32768"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
        ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

multi_AI_agent=Agent(
    team=(web_search_agent,finance_agent),
    instructions=["Always inclue sources","Use table to display data"],
    show_tool_calls=True,
    markdown=True
)

multi_AI_agent.print_response("Summarize analyst recommendation and share the latest news for Yes Bank", stream=True)
