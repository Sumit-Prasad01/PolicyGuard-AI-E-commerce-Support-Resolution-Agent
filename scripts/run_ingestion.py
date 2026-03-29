from src.policy_lens_agent.ingestion.pipeline import IngestionPipeline
from src.policy_lens_agent.utils.logger import logger
DATA_PATH = "data/raw"


def main():
    pipeline = IngestionPipeline(DATA_PATH)
    documents = pipeline.run()

    logger.info(f" Ingestion complete. Total chunks: {len(documents)}")


if __name__ == "__main__":
    main()