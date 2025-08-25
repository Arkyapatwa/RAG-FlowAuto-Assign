from abc import ABC, abstractmethod
from typing import List
from langchain_core.documents import Document

class ETLPipeline(ABC):
    @abstractmethod
    async def extract_data(self, file_path: str) -> None:
        """Extract, transform, load PDF into search backend."""
        pass
    
    @abstractmethod
    async def transform_data(self, documents: List[Document]) -> None:
        """Transform extracted data."""
        pass
    
    @abstractmethod
    async def load_data(self, docs: List[Document]) -> None:
        """Load transformed data into search backend."""
        pass
    
    @abstractmethod
    async def run(self, file_path: str) -> None:
        """Run the ETL pipeline."""
        pass
