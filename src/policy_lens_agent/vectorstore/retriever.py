from typing import List
from langchain_core.documents import Document
from src.policy_lens_agent.utils.logger import logger

class Retriever:
    def __init__(self, vectorstore, k: int = 5):
        self.vectorstore = vectorstore
        self.k = k

    def retrieve(self, query: str) -> List[Document]:
        logger.info("Retrieving Results...")

        results = self.vectorstore.similarity_search(query, k=self.k)

        logger.info("Results retrieved successfully..")
        return results

    def format_results(self, docs: List[Document]) -> List[dict]:
        formatted = []

        logger.info("Formatting Results...")

        for doc in docs:
            formatted.append({
                "text": doc.page_content,
                "source": doc.metadata.get("source", "unknown"),
                "chunk_id": doc.metadata.get("chunk_id", None)
            })
        
        logger.info("Results formatted successfully.")

        return formatted