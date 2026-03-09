from fastapi import FastAPI
from app.routers import base

app = FastAPI(
    title="Intern FastAPI Backend",
    description="Task 2 - FastAPI Structure",
    version="1.0.0"
)

app.include_router(base.router)


@app.get("/")
def root():
    """
    Root endpoint kiểm tra server hoạt động
    """
    return {"message": "API is running"}