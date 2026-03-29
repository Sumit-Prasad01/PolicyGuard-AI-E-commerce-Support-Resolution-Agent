from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):
    ticket: str
    order_context: Dict[str, Any]

    triage: Dict[str, Any]
    policy_evidence: List[Dict[str, Any]]
    resolution: Dict[str, Any]
    compliance: Dict[str, Any]

    stage: str