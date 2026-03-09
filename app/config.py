from dotenv import load_dotenv
import os

# Load biến môi trường từ .env
load_dotenv()


class Settings:
    """
    Class quản lý cấu hình dự án
    """

    APP_NAME = os.getenv("APP_NAME")

    DEBUG = os.getenv("DEBUG")

    SECRET_KEY = os.getenv("SECRET_KEY")

    ALGORITHM = os.getenv("ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


settings = Settings()