from utils.langchain_utils import init_gemini_model
from langchain_core.messages import HumanMessage, AIMessage

llm = init_gemini_model()

chat_history = []

chat_history.append(HumanMessage(content="Hi!Help me to understand what is LLM?"))

response = llm.invoke(chat_history)
chat_history.append(AIMessage(content=response.content))

print("AI:", response.content)

chat_history.append(HumanMessage(content="what are the applications of LLM?"))

response = llm.invoke(chat_history)
chat_history.append(AIMessage(content=response.content))

print("AI:", response.content)