from langchain_google_genai import ChatGoogleGenerativeAI

from backend.core.config import settings


class GeminiService:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.3,
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content


gemini_service = GeminiService()