import json
from typing import Dict, Any

from src.policy_lens_agent.models.llm import build_chain
from src.policy_lens_agent.prompts.templates import SYSTEM_PROMPT, COMPLIANCE_PROMPT


class ComplianceAgent:
    def __init__(self):
        self.chain = build_chain(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=COMPLIANCE_PROMPT
        )

    def run(self, resolution_output: Dict[str, Any]) -> Dict[str, Any]:
        user_input = f"""
Resolution Output:
{json.dumps(resolution_output, indent=2)}
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
                "status": "REJECTED",
                "reason": "Parsing error in compliance agent",
                "fix": "Ensure output follows strict JSON format with citations"
            }