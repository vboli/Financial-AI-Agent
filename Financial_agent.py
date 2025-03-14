from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import groq


web_search_agent= Agent(
    name= "web search Agent",
    role= "Search the web for the information",
    
    
    
)
