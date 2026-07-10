import fitz  # PyMuPDF

from backend.services.gemini_service import gemini_service
import json

class ReportService:

    def extract_text(self, pdf_path: str):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text


    def analyze(self, report_text: str):

        prompt = f"""
    You are an expert medical AI assistant.

    Analyze the following medical report.

    Return ONLY valid JSON.

    Do not write markdown.
    Do not write explanations.
    Do not use ```json.

    Return exactly this format:

    {{
        "summary": "...",
        "abnormal_findings":[
            "...",
            "..."
        ],
        "possible_conditions":[
            "...",
            "..."
        ],
        "recommendations":[
            "...",
            "..."
        ],
        "severity":"Low | Moderate | High | Critical",
        "confidence":95,

        "emergency":"YES | NO",

        "follow_up":"Consult within 24 hours",
        
        "disclaimer":"..."
    }}

    Medical Report:

    {report_text[:15000]}
    """

        response = gemini_service.generate(prompt)

        try:
            return json.loads(response)
        except Exception:
            return {
            "summary": response,
            "abnormal_findings": [],
            "possible_conditions": [],
            "recommendations": [],
            "severity": "Unknown",
            "confidence": 0,
            "emergency": "Unknown",
            "follow_up": "Consult your physician.",
            "disclaimer": "AI could not format the response."
        }


report_service = ReportService()