import json
from typing import Dict, Any, List

from src.policy_lens_agent.vectorstore.retriever import Retriever
from src.policy_lens_agent.models.llm import build_chain
from src.policy_lens_agent.prompts.templates import SYSTEM_PROMPT, RETRIEVER_PROMPT


class RetrieverAgent:
    def __init__(self, vectorstore):
        self.retriever = Retriever(vectorstore)
        self.chain = build_chain(
            system_prompt=SYSTEM_PROMPT,
            user_prompt=RETRIEVER_PROMPT
        )

    def run(self, query: str) -> List[Dict[str, Any]]:
        docs = self.retriever.retrieve(query)
        formatted_docs = self.retriever.format_results(docs)

        user_input = f"""
User Issue:
{query}

Retrieved Policy Chunks:
{json.dumps(formatted_docs, indent=2)}
"""

        response = self.chain.invoke({"input": user_input}).strip()

        try:
            return json.loads(response)
        except Exception:
            return formatted_docs