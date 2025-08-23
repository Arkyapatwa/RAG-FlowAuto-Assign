from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class SearchRepository(ABC):
    @abstractmethod
    def _index(self, doc: dict) -> None:
        """Create Index in the search backend."""
        pass

    @abstractmethod
    def search(self, top_k: int = 5) -> list[Document]:
        """Return top-k similar docs."""
        pass
    
    @abstractmethod
    async def add_documents(self, doc: List[Document]) -> None:
        """Add documents to the search backend."""
        pass
