from utils.langchain_utils import init_gemini_model
from langchain_core.messages import HumanMessage

llm = init_gemini_model()

input = "LLM stands for Large Language Model."
response = llm.invoke([HumanMessage(content="Summarize:\n" + input)]).content

response1 = llm.invoke([HumanMessage(content="Translate to Tamil:\n" + response)])

print("Final Output:", response1.content)   