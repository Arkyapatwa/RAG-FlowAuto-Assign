from abc import ABC, abstractmethod

class SearchService(ABC):
    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Search within a PDF."""
        pass
