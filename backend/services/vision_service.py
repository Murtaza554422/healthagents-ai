import json
from PIL import Image
import google.generativeai as genai

from backend.core.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)


class VisionService:

    def __init__(self):
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def analyze(self, image_path):

        image = Image.open(image_path)

        prompt = """
You are an expert medical vision assistant.

Analyze this medical image.

Return ONLY valid JSON.

{
  "image_type":"...",
  "findings":"...",
  "possible_conditions":[
      "...",
      "..."
  ],
  "severity":"Low |Moderate|High|Critical",
  "confidence":95,
  "recommendations":[
      "...",
      "..."
  ],
  "disclaimer":"This is not a medical diagnosis."
}
"""

        response = self.model.generate_content(
            [prompt, image]
        )

        return response.text


vision_service = VisionService()