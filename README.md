# AutoStream Agentic Sales Workflow

An AI-powered conversational agent designed for **AutoStream**, a SaaS platform for automated video editing. This agent identifies user intent, retrieves product information via RAG (Retrieval-Augmented Generation), and captures high-intent leads using tool-calling logic.

## ✨ Architecture 
<img width="2816" height="1536" alt="Architecture of autostream-agent excalidraww" src="https://github.com/user-attachments/assets/0cce155d-cb40-4762-9e17-8004256abeda" />

## Ui
<img width="2256" height="1377" alt="image" src="https://github.com/user-attachments/assets/09cee310-8ed3-496f-b71b-3d945167393b" />

## 🚀 Features
- **Intent Classification**: Categorizes queries into Greetings, Info (RAG), or High Intent.
- **RAG System**: Answers pricing and policy questions using a local JSON knowledge base.
- **Stateful Conversation**: Retains user context and lead details across multiple turns.
- **Lead Capture Tool**: Automatically triggers a mock API call once Name, Email, and Platform are collected.
- **Web UI**: Modern chat interface built with FastAPI and Tailwind CSS.

## 🛠️ Tech Stack
- **Language**: Python 3.13+
- **LLM**: Google Gemini 2.5 Flash
- **Orchestration**: LangChain (Agentic State Management logic)
- **Backend**: FastAPI
- **Frontend**: Vanilla JS & Tailwind CSS

## 📋 Prerequisites
- Python 3.9 or higher
- Google Gemini API Key (from [Google AI Studio](https://aistudio.google.com/))

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/autostream-agent.git
   cd autostream-agent


Create Virtual Environment
code Bash

    
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate    # Mac/Linux

  

Install Dependencies
code Bash

    
pip install -r requirements.txt

  

Environment Variables
Create a .env file in the root directory:
code Env

    
GOOGLE_API_KEY=your_gemini_api_key_here

  

Run the Application
code Bash

        
    python server.py    
    Open your browser at http://127.0.0.1:8000


Run Application in CLI
code Bash
        
    python main.py  


🏗️ Architecture Explanation (~200 words)

The AutoStream agent utilizes a Stateful Directed Acyclic Graph (DAG) architecture. I chose this approach (inspired by LangGraph principles) over a simple linear chain because sales conversations are non-linear. A user might start with a greeting, jump to pricing (RAG), and then suddenly express interest in signing up (Lead Capture).

Why this Architecture?

    Control: By separating Intent Detection from Response Generation, we prevent "hallucinations" regarding tool execution. The tool is only accessible if the HIGH_INTENT state is active.

    State Management: State is managed using a TypedDict structure called AgentState. This carries a is_collecting_lead boolean flag and a lead dictionary. This ensures that even if the LLM is called multiple times, the accumulated data (like the user's name) is persisted in the application layer, not just the model's transient memory.

    Scalability: This design allows us to add more "nodes" (e.g., a technical support node or a discount calculation node) without rewriting the core logic.

📱 WhatsApp Deployment Strategy

To integrate this agent with WhatsApp, I would use the WhatsApp Business Platform (Cloud API).

Steps for Integration:

    Webhook Setup: Create a FastAPI endpoint (e.g., /webhook) that accepts POST requests from Meta.

    Verification: Implement a GET handler for the endpoint to verify the "Webhook Token" required by Meta.

    Message Processing:

        When a user sends a message, Meta sends a JSON payload containing the sender's phone number (acting as the session_id) and the text.

        The backend processes this through the Agent logic.

    Response: Use the WhatsApp API's /messages endpoint to send the agent's response back to the user's phone number.

    Session Handling: Store the AgentState in a database (like Redis or MongoDB) keyed by the user's phone number to maintain state across the asynchronous nature of WhatsApp messages.

📂 Project Structure
code Text

    
autostream-agent/
├── agent/
│   ├── graph.py       # Lead capture & high-intent logic
│   ├── intent.py      # LLM Intent classification
│   ├── rag.py         # Knowledge retrieval logic
│   ├── state.py       # TypedDict state definitions
│   └── tools.py       # Mock lead capture function
├── data/
│   └── knowledge_base.json # Pricing & policies
├── static/
│   └── index.html     # Web UI
├── server.py          # FastAPI Backend
└── .env               # API Keys

  

code Code

    
### 3. Final steps for your assignment submission:
1. **Create the Repository**: Push your code to GitHub.
2. **Record the Video**: Use a tool like Loom or OBS.
    * Show yourself typing "What is the price?" (RAG).
    * Show yourself saying "I want to buy the Pro plan" (Intent shift).
    * Show the agent asking for Name, then Email, then Platform.
    * Point out the terminal log showing **"✅ LEAD CAPTURED SUCCESSFULLY"**.
3. **Double Check Files**: Make sure `requirements.txt` contains `langchain-google-genai`, `fastapi`, `uvicorn`, `python-dotenv`.

Good luck with your internship application! You now have a production-ready agentic structure.

  
  
    






   
