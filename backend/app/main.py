
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.core.config import settings

app = FastAPI()

# Read allowed frontend URLs from config.py
origins = [
    url.strip().rstrip("/")
    for url in settings.frontend_origins.split(",")
    if url.strip()
]

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins + [
        "http://localhost:3000",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "Plugin Chatbot API is running",
        "docs": "/docs",
    }
