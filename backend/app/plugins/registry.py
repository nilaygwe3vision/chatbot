from app.core.config import settings
from app.plugins.base import ChatProvider
from app.plugins.gemini.service import GeminiChatProvider

def get_chat_provider() -> ChatProvider:
    # Keep provider selection here so API routes don't depend on a specific vendor.
    return GeminiChatProvider(api_key=settings.gemini_api_key, model=settings.gemini_model)
