from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from utils.llm import get_gemini

search=DuckDuckGoSearchRun()

agent = create_agent(
    model=get_gemini(),
    tools=[search],
    system_prompt="")

result=agent.invoke({"messages":[{"role":"user","content":"Apllictaions of Langchain?"}]})
print(result)