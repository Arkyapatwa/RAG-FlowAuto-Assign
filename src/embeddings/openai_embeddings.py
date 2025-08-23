from embedding_generator_interface import EmbeddingGenerator
from src.conifg import OpenAIEmbeddingsConfig
from langchain_openai import OpenAIEmbeddings

class OpenAIEmbeddingsGenerator(EmbeddingGenerator):
    def __init__(self, config: OpenAIEmbeddingsConfig):
        self.embeddings = OpenAIEmbeddings(
            model=config.model_name,
            openai_api_key=config.api_key
        )
    
    def get_embedding_client(self) -> dict:
        """Return embedding vector for given text."""
        return {
            "client": self.embeddings
        }