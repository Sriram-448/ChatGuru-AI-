from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()
app = FastAPI(title="Groq Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Groq
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

# In-memory chat sessions
chat_sessions = {}

class MessageRequest(BaseModel):
    session_id: str
    message: str

class MessageResponse(BaseModel):
    reply: str
    session_id: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    try:
        session_id = request.session_id

        # Get or create chat history
        if session_id not in chat_sessions:
            chat_sessions[session_id] = [
                {"role": "system", "content": "You are a helpful and friendly AI assistant."}
            ]

        # Add user message to history
        chat_sessions[session_id].append({
            "role": "user",
            "content": request.message
        })

        # Call Groq API
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_sessions[session_id],
            max_tokens=1024,
        )

        reply = response.choices[0].message.content

        # Add assistant reply to history
        chat_sessions[session_id].append({
            "role": "assistant",
            "content": reply
        })

        return MessageResponse(reply=reply, session_id=session_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/chat/{session_id}")
async def clear_chat(session_id: str):
    if session_id in chat_sessions:
        del chat_sessions[session_id]
    return {"message": "Chat cleared"}
