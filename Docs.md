```
policy-lens-agent/
│
├── data/
│   ├── raw/                  # policy docs
│   ├── processed/
│   └── sources.md            # REQUIRED
│
├── src/
│   └── policy_agent/
│
│       ├── ingestion/
│       │   ├── loader.py
│       │   ├── chunker.py
│       │   └── pipeline.py
│
│       ├── vectorstore/
│       │   ├── faiss_store.py
│       │   └── retriever.py
│
│       ├── agents/
│       │   ├── triage_agent.py
│       │   ├── retriever_agent.py
│       │   ├── resolution_agent.py
│       │   ├── compliance_agent.py
│       │   └── orchestrator.py
│
│       ├── prompts/
│       │   └── templates.py
│
│       ├── models/
│       │   └── llm.py
│
│       └── utils/
│           └── helpers.py
│
├── evaluation/
│   ├── test_cases.json
│   └── evaluator.py
│
├── scripts/
│   ├── run_ingestion.py
│   ├── build_index.py
│   └── run_agent.py
│
├── demo/
│   └── streamlit_app.py   # optional but strong
│
├── vector_db/
│   └── faiss_index/
│
├── .env
├── requirements.txt
└── README.md
```