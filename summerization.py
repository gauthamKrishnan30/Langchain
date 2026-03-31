from utils.langchain_utils import init_gemini_model
from langchain_core.messages import HumanMessage

llm = init_gemini_model()

text = """
An Large Language Model is a type of AI designed to understand, process, and generate human-like text using deep learning and vast datasets.
They are pre-trained on massive datasets to recognize patterns and predict the next token in a sequence.
"""

prompt = f"Summarize this in 2 lines:{text}"

response = llm.invoke([HumanMessage(content=prompt)])

print("Summary:\n", response.content)