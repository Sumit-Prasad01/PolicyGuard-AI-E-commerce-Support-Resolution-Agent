import json
from typing import Dict, Any

from policy_lens_agent.agents.triage_agent import TriageAgent
from policy_lens_agent.agents.retriever_agent import RetrieverAgent
from policy_lens_agent.agents.resolution_agent import ResolutionAgent
from policy_lens_agent.agents.compliance_agent import ComplianceAgent


class Orchestrator:
    def __init__(self, vectorstore):
        self.triage_agent = TriageAgent()
        self.retriever_agent = RetrieverAgent(vectorstore)
        self.resolution_agent = ResolutionAgent()
        self.compliance_agent = ComplianceAgent()

    def run(self, ticket: str, order_context: Dict[str, Any]) -> Dict[str, Any]:

        # 1. TRIAGE
        triage_output = self.triage_agent.run(ticket, order_context)

        # If clarifications needed → return early
        if triage_output.get("clarifying_questions"):
            return {
                "stage": "clarification_needed",
                "triage": triage_output
            }

        # 2. RETRIEVE
        query = f"{ticket} {json.dumps(order_context)}"
        policy_evidence = self.retriever_agent.run(query)

        # 3. RESOLUTION
        resolution_output = self.resolution_agent.run(
            ticket,
            order_context,
            policy_evidence
        )

        # 4. COMPLIANCE CHECK
        compliance_output = self.compliance_agent.run(resolution_output)

        # Retry once if rejected
        if compliance_output.get("status") == "REJECTED":
            resolution_output = self.resolution_agent.run(
                ticket,
                order_context,
                policy_evidence
            )
            compliance_output = self.compliance_agent.run(resolution_output)

        return {
            "stage": "completed",
            "triage": triage_output,
            "resolution": resolution_output,
            "compliance": compliance_output
        }