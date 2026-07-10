import os
import shutil

from fastapi import APIRouter, UploadFile, File

from backend.agents.vision_agent import vision_agent

router = APIRouter(tags=["Medical Vision"])

UPLOAD_FOLDER = "data/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/vision/upload")
async def upload_image(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return vision_agent.process(file_path)