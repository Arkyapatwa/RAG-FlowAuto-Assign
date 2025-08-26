from abc import ABC, abstractmethod
from models.search import SearchResponseModel

class SearchService(ABC):
    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> SearchResponseModel:
        """Search within a PDF."""
        pass
