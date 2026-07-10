import os
import shutil

from fastapi import APIRouter, File, UploadFile

from backend.services.report_service import report_service
from backend.agents.report_agent import report_agent

router = APIRouter(tags=["Medical Report"])

UPLOAD_FOLDER = "data/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/report/upload")
async def upload_report(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    report_text = report_service.extract_text(file_path)

    result = report_agent.process(report_text)

    return result