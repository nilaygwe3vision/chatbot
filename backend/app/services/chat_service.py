from app.plugins.registry import get_chat_provider
from app.schemas.chat import ChatTurn

async def send_message(message: str, history: list[ChatTurn]) -> str:
    cleaned = message.strip()
    if not cleaned:
        raise ValueError("Please enter a question.")
    provider = get_chat_provider()
    return await provider.reply(cleaned, history)
