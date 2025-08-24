from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class PDFParser(ABC):
    @abstractmethod
    def parse(self) -> list[dict]:
        """
        Extract unstructured data from PDF.
        """
        pass
    
    @abstractmethod
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        pass
