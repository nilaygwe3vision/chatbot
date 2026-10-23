from google import genai
from app.plugins.base import ChatProvider
from app.schemas.chat import ChatTurn

class GeminiChatProvider(ChatProvider):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    async def reply(self, message: str, history: list[ChatTurn]) -> str:
        if not self.api_key or self.api_key == "your_real_api_key_here":
            raise RuntimeError(
                "Gemini API key is missing. Add GEMINI_API_KEY to backend/.env and restart the backend."
            )

        # google-genai's generate_content call is synchronous; run it in a worker thread
        # so the FastAPI event loop stays responsive.
        import asyncio
        return await asyncio.to_thread(self._generate, message, history)

    def _generate(self, message: str, history: list[ChatTurn]) -> str:
        client = genai.Client(api_key=self.api_key)
        conversation = []
        for turn in history[-20:]:
            role = "user" if turn.role == "user" else "model"
            conversation.append({"role": role, "parts": [{"text": turn.content}]})
        conversation.append({"role": "user", "parts": [{"text": message}]})
        response = client.models.generate_content(
            model=self.model,
            contents=conversation,
            config={"system_instruction": "You are a helpful chatbot. Answer clearly and accurately. If you are unsure, say so."},
        )
        answer = (response.text or "").strip()
        return answer or "I couldn't create a response. Please try asking in a different way."
