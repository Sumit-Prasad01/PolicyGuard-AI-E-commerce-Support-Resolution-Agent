# PolicyLens Support Agent (LangGraph)

## 🚀 Overview
PolicyLens is a multi-agent Retrieval-Augmented Generation (RAG) system designed to resolve e-commerce customer support tickets using policy documents. It ensures responses are grounded, citation-backed, and safe.

---

## 🧠 Features
- Multi-agent architecture (LangGraph)
- Policy-grounded responses with citations
- No hallucination enforcement
- Compliance validation with retry loop
- Handles edge cases, conflicts, and ambiguity
- Streamlit demo UI

---

## 🏗️ Architecture
Triage Agent → Retriever Agent → Resolution Agent → Compliance Agent

Built using **LangGraph** with conditional routing and retry logic.

---

## 📂 Project Structure
```
policy-lens-agent/
│
├── data/
├── src/policy_lens_agent/
│   ├── ingestion/
│   ├── vectorstore/
│   ├── agents/
│   ├── graph/
│   ├── prompts/
│   ├── models/
│   └── utils/
│
├── evaluation/
├── scripts/
├── demo/
├── vector_db/
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd policy-lens-agent
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

Activate:
- Windows:
```bash
.venv\Scripts\activate
```
- Mac/Linux:
```bash
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables
Create `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Run Instructions

### 1. Build Vector Index
```bash
python scripts/build_index.py
```

### 2. Run Agent
```bash
python scripts/run_agent.py
```

### 3. Run Evaluation
```bash
python evaluation/evaluator.py
```

### 4. Run Demo UI
```bash
streamlit run demo/streamlit_app.py
```

---

## 📊 Evaluation
- 20 test cases:
  - 8 standard cases
  - 6 edge cases
  - 3 conflict cases
  - 3 not-in-policy cases

Metrics:
- Citation coverage
- Unsupported claims
- Escalation accuracy

---

## 📌 Example Output
```json
{
  "decision": "partial",
  "rationale": "...",
  "citations": [...],
  "customer_response": "...",
  "internal_notes": "..."
}
```

---

## 🔐 Safety & Compliance
- Strict no-hallucination policy
- Citation enforcement
- Compliance agent validates output
- Retry mechanism for invalid responses

---

## 📈 Future Improvements
- Add real-time API integration
- Improve retrieval with hybrid search
- Add memory for multi-turn conversations
- Deploy as production service

---
