# 🎬 AutoStream Agentic Sales Workflow

> An intelligent conversational agent for AutoStream, a SaaS platform for automated video editing. Built with LangChain and Google Gemini, this agent uses RAG and stateful conversation management to qualify leads and provide intelligent product information.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://www.langchain.com/)

## ✨ Architecture 
<img width="2816" height="1536" alt="Architecture of autostream-agent excalidraww" src="https://github.com/user-attachments/assets/0cce155d-cb40-4762-9e17-8004256abeda" />

## Ui
<img width="2256" height="1377" alt="image" src="https://github.com/user-attachments/assets/09cee310-8ed3-496f-b71b-3d945167393b" />


## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🎯 **Intent Classification** | Intelligently categorizes queries into Greetings, Information Requests, or High Intent signals |
| 🔍 **RAG System** | Retrieves accurate answers about pricing and policies from a local knowledge base |
| 💬 **Stateful Conversations** | Maintains context and lead details across multiple conversation turns |
| 📊 **Smart Lead Capture** | Automatically collects Name, Email, and Platform when purchase intent is detected |
| 🌐 **Modern Web UI** | Clean, responsive chat interface built with FastAPI and Tailwind CSS |

---

## 🛠️ Technology Stack

- **Language**: Python 3.9+
- **LLM Provider**: Google Gemini 2.5 Flash
- **Orchestration**: LangChain (Stateful Agentic Logic)
- **Backend Framework**: FastAPI
- **Frontend**: Vanilla JavaScript + Tailwind CSS
- **State Management**: TypedDict with DAG Architecture

---

## 🏗️ Architecture Overview

The AutoStream agent implements a **Stateful Directed Acyclic Graph (DAG)** architecture, chosen specifically for the non-linear nature of sales conversations.

### Why This Architecture?

**🎛️ Controlled Tool Execution**  
By separating Intent Detection from Response Generation, we prevent hallucinations around tool usage. The lead capture tool is only accessible when the `HIGH_INTENT` state is active.

**💾 Persistent State Management**  
State is managed through an `AgentState` TypedDict structure containing:
- `is_collecting_lead`: Boolean flag for lead capture mode
- `lead`: Dictionary storing collected user information

This ensures data persistence across multiple LLM calls, storing information at the application layer rather than relying on model memory.

**🔧 Scalable Design**  
The modular node-based architecture allows easy addition of new capabilities (technical support, discount calculations, etc.) without core logic rewrites.

---

## 📋 Prerequisites

Before you begin, ensure you have:
- Python 3.9 or higher installed
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/))
- Git for version control

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/autostream-agent.git
cd autostream-agent
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Run the Application

**Web Interface:**
```bash
python server.py
```
Then open your browser at `http://127.0.0.1:8000`

**CLI Interface:**
```bash
python main.py
```

---

## 📁 Project Structure

```
autostream-agent/
├── agent/
│   ├── graph.py          # Lead capture & high-intent logic
│   ├── intent.py         # LLM intent classification
│   ├── rag.py            # Knowledge retrieval system
│   ├── state.py          # TypedDict state definitions
│   └── tools.py          # Mock lead capture function
├── data/
│   └── knowledge_base.json    # Pricing & policy information
├── static/
│   └── index.html        # Web UI interface
├── server.py             # FastAPI backend server
├── main.py               # CLI entry point
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
└── README.md            # Project documentation
```

---

## 📱 WhatsApp Deployment Strategy

### Integration Approach

To deploy this agent on WhatsApp, we leverage the **WhatsApp Business Platform (Cloud API)**.

### Implementation Steps

**1. Webhook Configuration**
- Create a FastAPI endpoint `/webhook` to receive POST requests from Meta
- Implement GET handler for webhook token verification

**2. Message Processing Pipeline**
```python
# Pseudocode flow
incoming_message = request.json
phone_number = incoming_message['from']  # Acts as session_id
user_text = incoming_message['text']

# Process through agent
response = agent.process(session_id=phone_number, message=user_text)

# Send response back via WhatsApp API
send_whatsapp_message(phone_number, response)
```

**3. State Persistence**
- Store `AgentState` in Redis or MongoDB
- Key by user's phone number for cross-message continuity
- Handle asynchronous nature of WhatsApp messaging

**4. Response Delivery**
- Use WhatsApp API's `/messages` endpoint
- Format responses for optimal mobile viewing
- Support rich media (buttons, lists) for better UX

---

## 🎯 Usage Example

**Sample Conversation Flow:**

```
User: What is the price?
Agent: [RAG Response] Our pricing starts at $29/month for the Basic plan...

User: I want to buy the Pro plan
Agent: [Intent: HIGH_INTENT] Great! I'll help you get started. What's your name?

User: John Doe
Agent: Thanks John! What's your email address?

User: john@example.com
Agent: Perfect! Which platform do you primarily create content for?

User: YouTube
Agent: ✅ Thank you! Your information has been recorded...
```

**Terminal Output:**
```
✅ LEAD CAPTURED SUCCESSFULLY
Name: John Doe
Email: john@example.com
Platform: YouTube
```

---

## 🔑 Key Dependencies

```txt
langchain-google-genai
fastapi
uvicorn
python-dotenv
pydantic
```

---

## 🚀 Future Enhancements

- [ ] Add multi-language support
- [ ] Implement CRM integration (Salesforce, HubSpot)
- [ ] Add conversation analytics dashboard
- [ ] Expand knowledge base with vector embeddings
- [ ] Implement A/B testing for response variations

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📧 Contact

For questions or feedback, please reach out to [gkashish1985@gmail.com]

---

<div align="center">
  
**Built with ❤️ using LangChain and Google Gemini**

</div>
