import json
from typing import Dict, Any

from policy_lens_agent.models.llm import build_chain
from policy_lens_agent.prompts.templates import SYSTEM_PROMPT, TRIAGE_PROMPT


class TriageAgent:
    def __init__(self):
        self.chain = build_chain(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=TRIAGE_PROMPT
        )

    def run(self, ticket: str, order_context: Dict[str, Any]) -> Dict:
        user_input = f"""
Customer Ticket:
{ticket}

Order Context:
{json.dumps(order_context, indent=2)}
"""

        response = self.chain.invoke({"input": user_input})

        try:
            return json.loads(response)
        except Exception:
            return {
                "classification": "unknown",
                "confidence": 0.0,
                "missing_fields": [],
                "clarifying_questions": ["Could you provide more details about your issue?"]
            }