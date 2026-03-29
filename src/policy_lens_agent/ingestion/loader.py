import os
from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.documents import Document
from src.policy_lens_agent.utils.logger import logger

class DocumentLoader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    logger.info("Loading Docements.....")

    def load_documents(self) -> List[Document]:
        documents = []

        for root, _, files in os.walk(self.data_path):
            for file in files:
                file_path = os.path.join(root, file)

                if file.endswith(".txt"):
                    loader = TextLoader(file_path, encoding="utf-8")
                    docs = loader.load()

                elif file.endswith(".pdf"):
                    loader = PyPDFLoader(file_path)
                    docs = loader.load()

                else:
                    continue

                for doc in docs:
                    doc.metadata["source"] = file
                    doc.metadata["path"] = file_path

                documents.extend(docs)
        
        logger.info("Documents loaded successfully.......")

        return documents