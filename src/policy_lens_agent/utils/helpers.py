import json
from typing import Any, Dict


def safe_json_loads(text: str, default: Dict = None) -> Dict:
    try:
        return json.loads(text)
    except Exception:
        return default or {}


def format_ticket_input(ticket: str, order_context: Dict[str, Any]) -> str:
    return f"""
Customer Ticket:
{ticket}

Order Context:
{json.dumps(order_context, indent=2)}
"""


def build_query(ticket: str, order_context: Dict[str, Any]) -> str:
    return f"{ticket} {json.dumps(order_context)}"