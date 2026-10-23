from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.core.config import settings



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://chatbot-frontend-4bii.onrender.com",
        "https://chatbot-render-frontend-iblfv5vag-w3-ed71.vercel.app/",
        "https://your-frontend.vercel.app",
        "https://chatbot-render-frontend.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["https://chatbot-frontend-4bii.onrender.com",
        "https://chatbot-render-frontend-iblfv5vag-w3-ed71.vercel.app/",
        "https://your-frontend.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500",],
    allow_headers=["https://chatbot-frontend-4bii.onrender.com",
        "https://chatbot-render-frontend-iblfv5vag-w3-ed71.vercel.app/",
        "https://your-frontend.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500",],
)

app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Plugin Chatbot API is running", "docs": "/docs"}
