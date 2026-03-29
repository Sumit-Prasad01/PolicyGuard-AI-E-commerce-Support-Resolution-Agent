from src.policy_lens_agent.ingestion.pipeline import IngestionPipeline
from src.policy_lens_agent.vectorstore.faiss_store import FAISSStore
from src.policy_lens_agent.utils.logger import logger


DATA_PATH = "data/raw"


def main():
    # Step 1: Ingest + Chunk
    pipeline = IngestionPipeline(DATA_PATH)
    documents = pipeline.run()
    logger.info(f"Loaded and chunked {len(documents)} documents")

    # Step 2: Build FAISS index
    store = FAISSStore()
    store.build_index(documents)

    # Step 3: Save index
    store.save_index()

    logger.info("FAISS index built and saved successfully")


if __name__ == "__main__":
    main()