from google import genai
from langchain_core.language_models import LLM
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class GoogleGemini(LLM):
    model: str = "gemini-2.5-flash"  
    temperature: float = 0.9

    def _call(self, prompt: str, stop=None):
        response = client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text

    @property
    def _identifying_params(self):
        return {"model": self.model, "temperature": self.temperature}
    
    @property
    def _llm_type(self) -> str:
        return "google_gemini"
