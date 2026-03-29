import json
from typing import Dict, Any, List

from src.policy_lens_agent.models.llm import build_chain
from src.policy_lens_agent.prompts.templates import SYSTEM_PROMPT, RESOLUTION_PROMPT


class ResolutionAgent:
    def __init__(self):
        self.chain = build_chain(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=RESOLUTION_PROMPT
        )

    def run(
        self,
        ticket: str,
        order_context: Dict[str, Any],
        policy_evidence: List[Dict[str, Any]]
    ) -> Dict:

        user_input = f"""
Customer Ticket:
{ticket}

Order Context:
{json.dumps(order_context, indent=2)}

Policy Evidence:
{json.dumps(policy_evidence, indent=2)}
"""

        response = self.chain.invoke({"input": user_input}).strip()

        # Extract JSON safely
        start = response.find("{")
        end = response.rfind("}") + 1

        try:
            if start != -1 and end != -1:
                response = response[start:end]

            return json.loads(response)

        except Exception:
            return {
                "decision": "escalate",
                "rationale": "Model output parsing failed",
                "citations": [],
                "customer_response": "We are reviewing your request and will get back to you shortly.",
                "internal_notes": "Parsing error in resolution agent"
            }