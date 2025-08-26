from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class PDFParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> list[dict]:
        """
        Extract unstructured data from PDF.
        """
        pass
    
    @abstractmethod
    def parse_images(self, file_path: str) -> List[Document]:
        """Extract and parse images from PDF."""
        pass
    
    @abstractmethod
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        pass
