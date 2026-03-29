from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from src.policy_lens_agent.utils.logger import logger

class DocumentChunker:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        chunks = self.splitter.split_documents(documents)

        logger.info("Creating chunks....")
        # Add chunk_id for traceability
        for i, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = i
        
        logger.info("Chunks created successfully.....")

        return chunks