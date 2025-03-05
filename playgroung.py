from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import phi.api
import phi
from phi.playground import Playground, serve_playground_app
from phi.model.openai import OpenAIChat
load_dotenv()


## Web Search Agent
web_search_agent = Agent(
    name="Web search Agent",
    role="Search the web for the information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always inclue sources"],
    show_tool_calls=True,
    markdown=True

)

## Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
        ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True                  
)

app = Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__ == '__main__':
    serve_playground_app("playgroung:app", reload=True)
