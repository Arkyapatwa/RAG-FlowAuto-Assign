from abc import ABC, abstractmethod

class PDFParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> list[dict]:
        """
        Extract structured data from PDF.
        Returns: list of {"page": int, "type": str, "content": str}
        """
        pass
