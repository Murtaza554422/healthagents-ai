import json

from backend.services.vision_service import vision_service


class VisionAgent:

    def process(self, image_path):

        response = vision_service.analyze(image_path)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        try:
            result = json.loads(response)

            return {
                "agent": "Medical Vision AI",
                **result
            }

        except Exception:

            return {
                "agent": "Medical Vision AI",
                "analysis": response
            }


vision_agent = VisionAgent()