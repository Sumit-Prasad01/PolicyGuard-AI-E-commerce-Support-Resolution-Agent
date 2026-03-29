import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "policy_lens_agent"

list_of_files = [

    # ---------------- DATA ----------------
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/sources.md",

    # ---------------- SOURCE ----------------
    f"src/{project_name}/__init__.py",

    # INGESTION
    f"src/{project_name}/ingestion/__init__.py",
    f"src/{project_name}/ingestion/loader.py",
    f"src/{project_name}/ingestion/chunker.py",
    f"src/{project_name}/ingestion/pipeline.py",

    # VECTOR STORE
    f"src/{project_name}/vectorstore/__init__.py",
    f"src/{project_name}/vectorstore/faiss_store.py",
    f"src/{project_name}/vectorstore/retriever.py",

    # AGENTS
    f"src/{project_name}/agents/__init__.py",
    f"src/{project_name}/agents/triage_agent.py",
    f"src/{project_name}/agents/retriever_agent.py",
    f"src/{project_name}/agents/resolution_agent.py",
    f"src/{project_name}/agents/compliance_agent.py",
    f"src/{project_name}/agents/orchestrator.py",

    # PROMPTS
    f"src/{project_name}/prompts/templates.py",

    # MODELS
    f"src/{project_name}/models/llm.py",

    # UTILS
    f"src/{project_name}/utils/helpers.py",

    # ---------------- EVALUATION ----------------
    "evaluation/test_cases.json",
    "evaluation/evaluator.py",

    # ---------------- SCRIPTS ----------------
    "scripts/run_ingestion.py",
    "scripts/build_index.py",
    "scripts/run_agent.py",

    # ---------------- DEMO ----------------
    "demo/streamlit_app.py",

    # ---------------- VECTOR DB ----------------
    "vector_db/faiss_index/.gitkeep",

    # ---------------- ROOT ----------------
    ".env",
    "requirements.txt",
    "README.md"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")

    if not os.path.exists(filepath):
        with open(filepath, 'w'):
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"{filename} already exists")