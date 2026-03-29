from src.policy_lens_agent.vectorstore.faiss_store import FAISSStore
from src.policy_lens_agent.graph.workflow import PolicyGraph
from src.policy_lens_agent.utils.logger import logger

def main():
    store = FAISSStore()
    vectorstore = store.load_index()

    graph = PolicyGraph(vectorstore).build()

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

    result = graph.invoke({
        "ticket": ticket,
        "order_context": order_context
    })

    logger.info("\n===== FINAL OUTPUT =====\n")
    import json
    logger.info(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()