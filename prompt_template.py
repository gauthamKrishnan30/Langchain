from utils.langchain_utils import init_gemini_model
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage

llm = init_gemini_model()

template= "Respond to the following question in a concise manner: {question}"

prompt= PromptTemplate(template=template, input_variables=["question"])

user_sentence = "What is LLM stands for?"

formatted_prompt = prompt.format(question=user_sentence)

response=llm.invoke([HumanMessage(content=formatted_prompt)])

print("user input:",user_sentence)
print("Langchain response:",response.content)