from backend.services.report_service import report_service


class ReportAgent:

    def process(self, report_text: str):

        result = report_service.analyze(report_text)

        return {
            "agent": "Medical Report Analyzer",
            **result
        }


report_agent = ReportAgent()