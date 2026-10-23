
import logging

from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import send_message

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        reply = await send_message(
            request.message,
            request.history
        )
        return ChatResponse(reply=reply)

    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc)
        ) from exc

    except RuntimeError as exc:
        logger.exception("Chat provider configuration or runtime error")
        raise HTTPException(
            status_code=503,
            detail=str(exc)
        ) from exc

    except Exception as exc:
        logger.exception("Chat provider failed")
        raise HTTPException(
            status_code=502,
            detail=f"Chat provider error: {type(exc).__name__}: {exc}"
        ) from exc
