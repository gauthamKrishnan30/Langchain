from utils.langchain_utils import init_gemini_model
from langchain_core.messages import SystemMessage, HumanMessage

llm = init_gemini_model()

messages = [
    SystemMessage(content="You are a python expert."),
    HumanMessage(content="Explain inheritance in simple terms")
]

response = llm.invoke(messages)

print("Response:", response.content)