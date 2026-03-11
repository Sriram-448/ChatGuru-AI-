# 🏴‍☠️ ChatGuru AI

## 🌐 Live Demo
👉 **[Try ChatGuru Live!](https://chatguru-ai.netlify.app)**

> *"I'm gonna be the King of the Pirates!"* - And you're gonna be the master of AI chat.

**ChatGuru** is a full-stack AI chatbot powered by **Groq's LLaMA 3.3 70B** model, built with a **FastAPI** backend and a One Piece themed frontend with splash screen animations, floating particles, and a rotating sunray background.

---

## ✨ Features

-  **LLaMA 3.3 70B** - lightning-fast AI responses via Groq
-  **One Piece themed UI** - animated splash screen with both images
-  **Rotating sunray background** inspired by Luffy's iconic pose
-  **Floating gold particles** and smooth animations
-  **Typing indicator** while AI is thinking
-  **Multi-turn conversation memory** per session
-  **Secure API key** management via `.env`
-  **Fully responsive** - works on mobile and desktop
-  **"Set Sail!" splash screen** on every launch

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                     USER BROWSER                     │
│                                                      │
│   ┌──────────────────────────────────────────────┐   │
│   │           Frontend (index.html)              │   │
│   │                                              │   │
│   │  ┌─────────────┐    ┌─────────────────────┐  │   │
│   │  │ Splash      │    │   Chat Interface    │  │   │
│   │  │ Screen      │ -  │                     │  │   │
│   │  │             │    │  ┌───────────────┐  │  │   │
│   │  │ onepiece-1  │    │  │  Chat Bubble  │  │  │   │
│   │  │ onepiece-2  │    │  │  Typing Dots  │  │  │   │
│   │  │ Animations  │    │  │  Input Box    │  │  │   │
│   │  └─────────────┘    │  └───────────────┘  │  │   │
│   │                     └─────────────────────┘  │   │
│   └──────────────────┬───────────────────────────┘   │
│                      │  HTTP POST /chat               │
└──────────────────────┼──────────────────────────────-┘
                       │
                       
┌─────────────────────────────────────────────────────┐
│              Backend (FastAPI - Port 8000)           │
│                                                      │
│   ┌──────────────────────────────────────────────┐   │
│   │                  main.py                     │   │
│   │                                              │   │
│   │   POST /chat - Session Manager             │   │
│   │   DELETE /chat - Clear History             │   │
│   │   GET /health - Status Check               │   │
│   │                                              │   │
│   │   ┌────────────────────────────────────┐     │   │
│   │   │        Chat Session Store          │     │   │
│   │   │  { session_id: [messages...] }     │     │   │
│   │   └────────────────────────────────────┘     │   │
│   └──────────────────┬───────────────────────────┘   │
│                      │                               │
│   ┌────────────────── .  ───────────────────────────┐   │
│   │              .env (Secret)                   │   │
│   │         GROQ_API_KEY=gsk_xxxx                │   │
│   └──────────────────┬───────────────────────────┘   │
└──────────────────────┼──────────────────────────────-┘
                       │  HTTPS API Call
                       
┌─────────────────────────────────────────────────────┐
│                  Groq Cloud API                      │
│                                                      │
│         Model: llama-3.3-70b-versatile               │
│         Fast inference • Free tier                   │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
ChatGuru/
├── .gitignore                  - Hides .env from GitHub
├── README.md                   - You are here
│
├── Backend/
│   ├── main.py                 - FastAPI server & Groq integration
│   ├── requirements.txt        - Python dependencies
│   ├── .env                    - Your secret API key (NOT on GitHub)
│   └── .env.example            - Template for others
│
└── Frontend/
    ├── index.html              - Full chat UI with splash screen
    ├── onepiece-1.webp         - Luffy with flag background
    └── onepiece-2.webp         - Luffy smiling background
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com/keys)

### 1. Clone the repository
```bash
git clone https://github.com/Sriram-448/ChatGuru-AI-.git
cd ChatGuru-AI-
```

### 2. Set up the backend
```bash
cd Backend
pip install -r requirements.txt
```

### 3. Configure your API key
Create a `.env` file inside the `Backend` folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Start the backend server
```bash
python -m uvicorn main:app --reload --port 8000
```

### 5. Start the frontend server
Open a new terminal:
```bash
cd Frontend
python -m http.server 3000
```

### 6. Open your browser
```
http://localhost:3000
```

Click ** Set Sail!** and start chatting! 

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/chat` | Send a message, receive AI reply |
| `DELETE` | `/chat/{session_id}` | Clear conversation history |
| `GET` | `/health` | Server health check |

### Example Request
```json
POST /chat
{
  "session_id": "abc-123",
  "message": "Who is Monkey D. Luffy?"
}
```

### Example Response
```json
{
  "reply": "Monkey D. Luffy is the main protagonist of One Piece...",
  "session_id": "abc-123"
}
```

---

##  Security

- API key is stored in `.env` which is listed in `.gitignore`
- The `.env` file is **never uploaded to GitHub**
- Others cloning this repo must create their own `.env` with their own key

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| AI Model | LLaMA 3.3 70B via Groq |
| Backend | Python + FastAPI + Uvicorn |
| Frontend | HTML + CSS + Vanilla JavaScript |
| Fonts | Bangers + DM Mono (Google Fonts) |
| Styling | CSS Variables + Animations |

---

## 👨‍💻 Built by

**Sriram** - Built from scratch with 🏴‍☠️ and a lot of determination!

---

*"The only ones who should kill are those who are prepared to be killed."* - But the only ones who should code are those prepared to debug! 
