import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import retrieve_knowledge
from agent.graph import handle_high_intent

load_dotenv()

# Get the key from env
api_key = os.getenv("GOOGLE_API_KEY") 

# Initialize LLM correctly for LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",        # Removed "models/" prefix
    google_api_key=api_key,          # Pass key explicitly to be safe
    temperature=0
)

state: AgentState = {
    "messages": [],
    "intent": None,
    "is_collecting_lead": False,
    "lead": {
        "name": None,
        "email": None,
        "platform": None
    }
}


user_inputs = [
    "I want to try the Pro plan",
    "Ashish Gupta",
    "ashish@example.com",
    "YouTube"
]
for user_input in user_inputs:
    print("\nUser:", user_input)

    if state["intent"] is None:
        state["intent"] = detect_intent(llm, user_input)

    if state["intent"] == "HIGH_INTENT":
        response = handle_high_intent(state, user_input)
        print("Agent:", response)

    elif state["intent"] == "INFO":
        print("Agent:", retrieve_knowledge(user_input))

    else:
        print("Agent: Hello! How can I help you?")

# print("Detected intent:", intent)
# print("Updated state:", state)

