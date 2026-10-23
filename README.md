# Plugin-Based AI Chatbot (React + FastAPI)

A minimal chatbot starter with a modular/plugin-style backend. The React frontend and FastAPI backend can be run and deployed separately.

## Features
- Chat UI: user sends a question and sees the assistant reply.
- FastAPI endpoint: `POST /api/chat`
- Health endpoint: `GET /api/health`
- LLM provider is isolated as a plugin so it can be replaced without changing API routes.
- If `GEMINI_API_KEY` is not configured, the backend returns a clear setup message instead of pretending to generate an AI answer.

## Folder structure

```text
plugin-chatbot/
├── backend/
│   ├── app/
│   │   ├── api/routes/chat.py       # HTTP endpoints only
│   │   ├── core/config.py           # environment configuration
│   │   ├── plugins/
│   │   │   ├── base.py              # provider interface
│   │   │   ├── registry.py          # chooses active provider
│   │   │   └── gemini/
│   │   │       ├── __init__.py
│   │   │       └── service.py       # Gemini API integration
│   │   ├── schemas/chat.py          # request/response models
│   │   ├── services/chat_service.py # app-level chat orchestration
│   │   └── main.py                  # FastAPI app entry point
│   ├── .env.example
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/ChatMessage.jsx
    │   ├── services/chatApi.js
    │   ├── App.jsx
    │   ├── main.jsx
    │   └── styles.css
    ├── .env.example
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## 1. Run backend (Windows PowerShell)

Open a terminal in `backend`:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `backend/.env` and set your Gemini API key:

```env
GEMINI_API_KEY=your_real_api_key_here
GEMINI_MODEL=gemini-2.5-flash
FRONTEND_ORIGINS=http://localhost:5173
```

Start the API:

```powershell
uvicorn app.main:app --reload
```

Backend URL: `http://127.0.0.1:8000`  
API docs: `http://127.0.0.1:8000/docs`

## 2. Run frontend

Open a second terminal in `frontend`:

```powershell
npm install
Copy-Item .env.example .env
npm run dev
```

Open the Vite URL shown in the terminal (usually `http://localhost:5173`).

The frontend `.env` should contain:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## How plugin isolation works

The route calls `chat_service`, which gets the active provider from `plugins/registry.py`. The Gemini implementation is inside `plugins/gemini/service.py`. To add another provider, implement `ChatProvider` in a new plugin and update the registry. Keep API routes and React UI independent of the provider.

Deleting a file can still break anything that imports it; this structure reduces coupling, but files should be removed only after updating their imports/configuration.

## Important
- Never commit `.env` or publish your API key.
- This is a starter chatbot, not a production-hardened service. Before production, add authentication, rate limits, logging, and deployment-specific CORS settings.
