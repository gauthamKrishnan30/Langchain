from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os

from typer import prompt

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9,
)

prompt1=PromptTemplate(input_variables=["subject"], template="explain about {subject}")

prompt2=PromptTemplate(input_variables=["topic"], template="What is {topic}?")

chain = prompt1 | llm | (lambda x: {"topic": x}) | prompt2 | llm


def get_response(user_input):
    response = chain.invoke({"subject": user_input})
    return response.content


