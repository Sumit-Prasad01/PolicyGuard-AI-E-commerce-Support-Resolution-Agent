import streamlit as st
import json

from policy_lens_agent.vectorstore.faiss_store import FAISSStore
from policy_lens_agent.agents.orchestrator import Orchestrator

st.title("🧠 PolicyLens Support Agent")

ticket = st.text_area("Enter Customer Ticket")

order_context = st.text_area("Enter Order Context (JSON)", value="""
{
  "order_date": "2026-03-20",
  "delivery_date": "2026-03-25",
  "item_category": "perishable",
  "fulfillment_type": "first-party",
  "shipping_region": "India",
  "order_status": "delivered"
}
""")

if st.button("Run Agent"):
    store = FAISSStore()
    vectorstore = store.load_index()

    agent = Orchestrator(vectorstore)

    try:
        context_json = json.loads(order_context)
        result = agent.run(ticket, context_json)

        st.json(result)

    except Exception as e:
        st.error(str(e))