from typing import List
from langchain_core.documents import Document

from .loader import DocumentLoader
from .chunker import DocumentChunker

from src.policy_lens_agent.utils.logger import logger

class IngestionPipeline:
    def __init__(self, data_path: str):
        self.loader = DocumentLoader(data_path)
        self.chunker = DocumentChunker()

    logger.info("Processing data......")

    def run(self) -> List[Document]:
        # Load raw documents
        documents = self.loader.load_documents()

        # Chunk documents
        chunks = self.chunker.chunk_documents(documents)

        logger.info("Data processed successfully.")

        return chunks