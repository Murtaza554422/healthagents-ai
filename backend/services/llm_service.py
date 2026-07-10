from langchain_fireworks import ChatFireworks
from backend.core.config import settings


class LLMService:
    def __init__(self):
        self.llm = ChatFireworks(
            model="accounts/fireworks/models/kimi-k2p7-code",
            fireworks_api_key=settings.FIREWORKS_API_KEY,
            temperature=0.3,
            max_tokens=1024,
        )

    def chat(self, message: str):
        response = self.llm.invoke(message)
        return response.content


llm_service = LLMService()