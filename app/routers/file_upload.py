from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter(prefix="/file", tags=["file"])


UPLOAD_DIR = "utils/upload_temp"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    API upload file lên server
    """

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "filename": file.filename,
        "message": "Upload successful"
    }