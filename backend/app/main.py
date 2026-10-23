from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.core.config import settings

app = FastAPI(title="Plugin Chatbot API", version="1.0.0")

origins = [item.strip() for item in settings.frontend_origins.split(",") if item.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chatbot-frontend-4bii.onrender.com",
        "https://chatbot-frontend-4bii.onrender.com/",
        "https://chatbot-render-frontend.vercel.app/",
        "https://chatbot-render-frontend.vercel.app/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Plugin Chatbot API is running", "docs": "/docs"}
