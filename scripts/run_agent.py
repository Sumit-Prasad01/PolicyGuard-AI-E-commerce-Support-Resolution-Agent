import json

from policy_lens_agent.vectorstore.faiss_store import FAISSStore
from policy_lens_agent.agents.orchestrator import Orchestrator
from src.policy_lens_agent.utils.logger import logger

def main():
    # Load FAISS index
    store = FAISSStore()
    vectorstore = store.load_index()

    # Initialize orchestrator
    agent = Orchestrator(vectorstore)

    # Sample input
    ticket = "My order arrived late and the cookies are melted. I want a full refund and to keep the item."

    order_context = {
        "order_date": "2026-03-20",
        "delivery_date": "2026-03-25",
        "item_category": "perishable",
        "fulfillment_type": "first-party",
        "shipping_region": "India",
        "order_status": "delivered",
        "payment_method": "prepaid"
    }

    # Run agent
    result = agent.run(ticket, order_context)

    logger.info("\n===== FINAL OUTPUT =====\n")
    logger.info(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()