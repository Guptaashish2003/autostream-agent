from typing import TypedDict, List, Optional


class LeadInfo(TypedDict):
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]


class AgentState(TypedDict):
    messages: List[str]
    intent: Optional[str]
    lead: LeadInfo
    is_collecting_lead: bool
