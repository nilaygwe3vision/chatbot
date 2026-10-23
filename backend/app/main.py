from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.core.config import settings

app = FastAPI(title="Plugin Chatbot API", version="1.0.0")

raw_origins = [item.strip() for item in settings.frontend_origins.split(",") if item.strip()]
origins = ["*"] if ("*" in raw_origins or not raw_origins) else raw_origins

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Plugin Chatbot API is running", "docs": "/docs"}
