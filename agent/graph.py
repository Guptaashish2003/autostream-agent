from agent.state import AgentState
from agent.tools import mock_lead_capture


def handle_high_intent(state: AgentState, user_input: str):
    lead = state["lead"]

    # 🚫 First HIGH_INTENT message → do NOT store
    if not state["is_collecting_lead"]:
        state["is_collecting_lead"] = True
        return "Great! Could you please share your name?"

    # Step 1: Name
    if lead["name"] is None:
        lead["name"] = user_input
        return "Thanks! Could you share your email address?"

    # Step 2: Email
    if lead["email"] is None:
        lead["email"] = user_input
        return "Which platform do you create content on? (YouTube, Instagram, etc.)"

    # Step 3: Platform
    if lead["platform"] is None:
        lead["platform"] = user_input

        mock_lead_capture(
            name=lead["name"],
            email=lead["email"],
            platform=lead["platform"]
        )

        return "🎉 You're all set! Our team will reach out to you shortly."

    return "Lead already captured."
