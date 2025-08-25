from langchain_core.documents import Document
from parsers.pdfparser_interface import PDFParser
from repositories.search_repository_interface import SearchRepository
from pipelines.etl_pipeline_interface import ETLPipeline 
from embeddings.embedding_generator_interface import EmbeddingGenerator
from typing import List
import uuid

class PDFRAGETLPipeline(ETLPipeline):
    def __init__(self, parser: PDFParser, repository: SearchRepository, embeddings: EmbeddingGenerator):
        self.parser = parser
        self.repository = repository
        self.embeddings = embeddings
        
    async def extract_data(self, file_path: str) -> List[Document]:
        documents = self.parser.parse(file_path)
        return documents
    
    async def transform_data(self, documents: List[Document]) -> List[Document]:
        split_docs = self.parser.split_documents(documents)
        return split_docs
    
    async def load_data(self, docs: List[Document]) -> None:
        ids = [str(uuid.uuid4()) for _ in range(len(docs))]
        await self.repository.add_documents(docs, ids)
        
    async def run(self, file_path: str) -> None:
        extracted_docs = await self.extract_data(file_path=file_path)
        transformed_docs = await self.transform_data(extracted_docs)
        await self.load_data(transformed_docs)
    