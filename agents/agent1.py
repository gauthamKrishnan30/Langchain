from langchain.agents import create_agent
from langchain.tools import tool
from utils.llm import get_gemini

@tool
def get_weather(city: str) -> str:
    """ Get current weather conditions for a given city. """

    return f"Weather in {city} is 25°C."

@tool
def calculate(expression: str) -> str:
    """ Calculate the result of a mathematical expression. """

    try:
        result = eval(expression)
        return f"The result of {expression} is {result}."   
    except:
        return "Invalid expression."

llm = get_gemini()
agent = create_agent(
    model=llm,
     tools= [get_weather],
     system_prompt="")

result=agent.invoke({"messages":[{"role":"user","content":"What's the weather in Thanjavur?"}]})
print(result)