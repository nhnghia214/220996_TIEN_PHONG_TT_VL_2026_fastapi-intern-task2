from fastapi import FastAPI
from app.routers import base, auth, file_upload
from app.config import settings

app = FastAPI(
    title="Intern FastAPI Backend",
    description="Task 2 - FastAPI Structure",
    version="1.0.0"
)

app.include_router(base.router)
app.include_router(auth.router)
app.include_router(file_upload.router)


@app.get("/")
def root():
    return {"message": "API is running"}


@app.get("/config-test")
def config_test():
    return {
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG
    }