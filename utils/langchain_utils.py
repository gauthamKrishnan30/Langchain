from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")  

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set") 
os.environ["GEMINI_API_KEY"] = api_key
def init_gemini_model(max_tokens=3000):
    """ Initialization of model"""
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.9, max_tokens=max_tokens)
    return llm