import os
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from src.policy_lens_agent.utils.logger import logger

class SentenceTransformerEmbeddings:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        logger.info("Embedding documents....")
        return self.model.encode(texts, show_progress_bar=True).tolist()

    def embed_query(self, text: str) -> List[float]:
        logger.info("Embedding user query....")
        return self.model.encode(text).tolist()


class FAISSStore:
    def __init__(self, embedding_model=None, index_path: str = "vector_db/faiss_index"):
        self.embedding_model = embedding_model or SentenceTransformerEmbeddings()
        self.index_path = index_path
        self.vectorstore = None

    def build_index(self, documents: List[Document]):
        texts = [doc.page_content for doc in documents]
        metadatas = [doc.metadata for doc in documents]

        self.vectorstore = FAISS.from_texts(
            texts=texts,
            embedding=self.embedding_model,
            metadatas=metadatas
        )

        return self.vectorstore

    def save_index(self):
        if not self.vectorstore:
            raise ValueError("No vectorstore to save")

        os.makedirs(self.index_path, exist_ok=True)
        self.vectorstore.save_local(self.index_path)

    def load_index(self):
        if not os.path.exists(self.index_path):
            raise ValueError("Index path does not exist")

        self.vectorstore = FAISS.load_local(
            self.index_path,
            embeddings=self.embedding_model,
            allow_dangerous_deserialization=True
        )

        return self.vectorstore