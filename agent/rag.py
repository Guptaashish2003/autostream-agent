import json
from pathlib import Path

# Path relative to project root
KB_PATH = Path("data/knowledge_base.json")

def load_kb():
    if not KB_PATH.exists():
        return {}
    try:
        with open(KB_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Return empty dict if file is empty or invalid JSON
        return {}

# Load it safely
KNOWLEDGE_BASE = load_kb()

def retrieve_knowledge(query: str) -> str:
    query = query.lower()

    if "price" in query or "plan" in query:
        return (
            "AutoStream Pricing:\n"
            "- Basic Plan: $29/month, 10 videos/month, 720p resolution\n"
            "- Pro Plan: $79/month, Unlimited videos, 4K resolution, AI captions"
        )

    if "refund" in query:
        return "Refund Policy: No refunds after 7 days."

    if "support" in query:
        return "Support Policy: 24/7 support is available only on the Pro plan."

    return "Sorry, I can help with pricing, plans, refunds, and support questions."