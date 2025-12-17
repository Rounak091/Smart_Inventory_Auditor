import os
from fastapi import APIRouter, UploadFile, File
from app.services.auditor_agent import audit_image
from app.core.config import settings

router = APIRouter()

os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

@router.post("/audit")
async def audit_inventory(image: UploadFile = File(...)):
    file_path = os.path.join(settings.UPLOAD_DIR, image.filename)

    with open(file_path, "wb") as f:
        f.write(await image.read())

    result = audit_image(file_path)

    return {
        "action_plan": result
    }
