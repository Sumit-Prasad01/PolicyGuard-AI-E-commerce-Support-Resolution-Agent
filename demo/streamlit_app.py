import streamlit as st
import json

from src.policy_lens_agent.vectorstore.faiss_store import FAISSStore
from src.policy_lens_agent.graph.workflow import PolicyGraph

st.title("🧠 PolicyLens Support Agent (LangGraph)")

ticket = st.text_area("Enter Customer Ticket")

order_context = st.text_area("Enter Order Context (JSON)", value="""
{
  "order_date": "2026-03-20",
  "delivery_date": "2026-03-25",
  "item_category": "perishable",
  "fulfillment_type": "first-party",
  "shipping_region": "India",
  "order_status": "delivered",
  "payment_method": "prepaid"
}
""")

if st.button("Run Agent"):
    try:
        # Load vectorstore
        store = FAISSStore()
        vectorstore = store.load_index()

        # Build LangGraph
        graph = PolicyGraph(vectorstore).build()

        # Parse input
        context_json = json.loads(order_context)

        # Run graph
        result = graph.invoke({
            "ticket": ticket,
            "order_context": context_json
        })

        st.success("✅ Execution Complete")
        st.json(result)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")