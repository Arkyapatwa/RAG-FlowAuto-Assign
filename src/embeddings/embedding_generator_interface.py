from abc import ABC, abstractmethod

class EmbeddingGenerator(ABC):
    @abstractmethod
    def get_embedding_client(self) -> dict:
        """Return embedding vector for given text."""
        pass
