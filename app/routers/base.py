from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """
    API kiểm tra trạng thái server
    """
    return {"status": "ok"}