class RouterAgent:

    def route(self, message: str):

        message = message.lower()

        if any(word in message for word in ["pain", "fever", "headache", "cough"]):
            return "symptom"

        elif any(word in message for word in ["report", "blood", "lab"]):
            return "report"

        elif any(word in message for word in ["xray", "x-ray", "mri", "ct", "image"]):
            return "vision"

        else:
            return "general"


router_agent = RouterAgent()