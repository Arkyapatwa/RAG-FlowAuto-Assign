from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import os
from parsers.pdfparser_interface import PDFParser


class PDFParserImpl(PDFParser):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self, file_path: str) -> List[Document]:
        """Parse PDF and return list of documents."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        loader = PyMuPDFLoader(file_path, extract_images=True, extract_tables='csv')
        documents = loader.load()
        print(f"Parsed {len(documents)} documents from {file_path}: {documents}")
        return documents
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=10,
            length_function=len,
        )
        split_docs = text_splitter.split_documents(documents)
        return split_docs