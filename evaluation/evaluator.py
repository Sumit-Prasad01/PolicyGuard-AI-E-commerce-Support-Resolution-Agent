import json
from policy_lens_agent.vectorstore.faiss_store import FAISSStore
from policy_lens_agent.agents.orchestrator import Orchestrator
from src.policy_lens_agent.utils.logger import logger

def evaluate():
    with open("evaluation/test_cases.json", "r") as f:
        test_cases = json.load(f)

    store = FAISSStore()
    vectorstore = store.load_index()

    agent = Orchestrator(vectorstore)

    results = []

    for case in test_cases:
        output = agent.run(case["ticket"], case["order_context"])

        results.append({
            "input": case,
            "output": output
        })

    with open("evaluation/results.json", "w") as f:
        json.dump(results, f, indent=2)

    logger.info("Evaluation complete")


if __name__ == "__main__":
    evaluate()