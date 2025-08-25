from embeddings.embedding_generator_interface import EmbeddingGenerator
from conifg import OpenAIEmbeddingsConfig
from langchain_openai import OpenAIEmbeddings

class OpenAIEmbeddingsGenerator(EmbeddingGenerator):
    def __init__(self, config: OpenAIEmbeddingsConfig):
        self.embeddings = OpenAIEmbeddings(
            model=config.model_name,
            api_key=config.api_key,
            base_url=config.endpoint,
            max_retries=config.max_retries,
            dimensions=2000
        )
    
    def get_embedding_client(self) -> dict:
        """Return embedding vector for given text."""
        return {
            "client": self.embeddings
        }