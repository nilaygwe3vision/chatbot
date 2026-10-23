import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "").strip()

    gemini_model: str = os.getenv(
        "GEMINI_MODEL", "gemini-2.5-flash"
    ).strip()

    frontend_origins: str = os.getenv(
        "FRONTEND_ORIGINS",
        "https://chatbot-frontend-4bii.onrender.com,"
        "https://chatbot-render-frontend.vercel.app"
    ).strip()

settings = Settings()
