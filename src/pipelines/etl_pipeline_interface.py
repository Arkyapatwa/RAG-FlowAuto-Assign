from abc import ABC, abstractmethod

class ETLPipeline(ABC):
    @abstractmethod
    def ingest(self, pdf_id: str, file_path: str) -> None:
        """Extract, transform, load PDF into search backend."""
        pass
