from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document
import uuid

class SearchRepository(ABC):
    @abstractmethod
    def _index(self, config) -> None:
        """Create Index in the search backend."""
        pass

    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> list[Document]:
        """Return top-k similar docs."""
        pass
    
    @abstractmethod
    async def add_documents(self, doc: List[Document], ids: List[str | uuid.UUID]) -> None:
        """Add documents to the search backend."""
        pass
