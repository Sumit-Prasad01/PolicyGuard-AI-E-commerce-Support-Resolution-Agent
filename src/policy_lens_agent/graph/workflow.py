from langgraph.graph import StateGraph, END

from src.policy_lens_agent.graph.state import AgentState
from src.policy_lens_agent.agents.triage_agent import TriageAgent
from src.policy_lens_agent.agents.retriever_agent import RetrieverAgent
from src.policy_lens_agent.agents.resolution_agent import ResolutionAgent
from src.policy_lens_agent.agents.compliance_agent import ComplianceAgent


class PolicyGraph:
    def __init__(self, vectorstore):
        self.triage = TriageAgent()
        self.retriever = RetrieverAgent(vectorstore)
        self.resolution = ResolutionAgent()
        self.compliance = ComplianceAgent()

    # ---------------- NODES ---------------- #

    def triage_node(self, state: AgentState):
        result = self.triage.run(state["ticket"], state["order_context"])
        return {"triage": result}

    def retrieve_node(self, state: AgentState):
        query = f"{state['ticket']} {state['order_context']}"
        evidence = self.retriever.run(query)
        return {"policy_evidence": evidence}

    def resolution_node(self, state: AgentState):
        result = self.resolution.run(
            state["ticket"],
            state["order_context"],
            state["policy_evidence"]
        )
        return {"resolution": result}

    def compliance_node(self, state: AgentState):
        result = self.compliance.run(state["resolution"])
        return {"compliance": result}

    # ---------------- ROUTING ---------------- #

    def compliance_router(self, state: AgentState):
        if state["compliance"]["status"] == "REJECTED":
            return "resolution"
        return END

    # ---------------- BUILD GRAPH ---------------- #

    def build(self):
        graph = StateGraph(AgentState)

        graph.add_node("triage", self.triage_node)
        graph.add_node("retrieve", self.retrieve_node)
        graph.add_node("resolution", self.resolution_node)
        graph.add_node("compliance", self.compliance_node)

        graph.set_entry_point("triage")

        graph.add_edge("triage", "retrieve")
        graph.add_edge("retrieve", "resolution")
        graph.add_edge("resolution", "compliance")

        graph.add_conditional_edges(
            "compliance",
            self.compliance_router
        )

        return graph.compile()