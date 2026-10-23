from abc import ABC, abstractmethod
from app.schemas.chat import ChatTurn

class ChatProvider(ABC):
    @abstractmethod
    async def reply(self, message: str, history: list[ChatTurn]) -> str:
        """Return an assistant response for the user message."""
        raise NotImplementedError
