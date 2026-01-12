import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Import your existing logic
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import retrieve_knowledge
from agent.graph import handle_high_intent

load_dotenv()

app = FastAPI()

# Global dictionary to store session state (In a real app, use Redis or a Database)
sessions = {}

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

def get_or_create_state(session_id: str) -> AgentState:
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "intent": None,
            "is_collecting_lead": False,
            "lead": {"name": None, "email": None, "platform": None}
        }
    return sessions[session_id]

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    state = get_or_create_state(req.session_id)
    user_input = req.message
    
    # 1. Logic to determine response
    # If we are already collecting lead info, stay in HIGH_INTENT mode
    if state["is_collecting_lead"]:
        intent = "HIGH_INTENT"
    else:
        intent = detect_intent(llm, user_input)
        state["intent"] = intent

    # 2. Generate Response based on Intent
    if intent == "HIGH_INTENT":
        response = handle_high_intent(state, user_input)
    elif intent == "INFO":
        response = retrieve_knowledge(user_input)
    elif intent == "GREETING":
        response = "Hello! I'm the AutoStream assistant. How can I help you with our video tools today?"
    else:
        response = "I'm not sure I understand. I can help with pricing, support, or setting up a Pro account!"

    state["messages"].append({"user": user_input, "agent": response})
    
    return {
        "response": response,
        "state": state # Send state back so UI can show progress
    }

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)