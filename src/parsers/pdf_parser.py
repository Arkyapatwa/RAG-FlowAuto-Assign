from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import os
from src.parsers.pdfparser_interface import PDFParser


class PDFParserImpl(PDFParser):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self) -> List[Document]:
        """Parse PDF and return list of documents."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        
        loader = PyMuPDFLoader(self.file_path, extract_images=True, extract_tables='csv')
        documents = loader.load()
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            length_function=len,
        )
        split_docs = text_splitter.split_documents(documents)
        return split_docs