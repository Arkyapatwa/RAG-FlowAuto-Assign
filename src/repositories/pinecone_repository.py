from search_repository_interface import SearchRepository
from src.conifg import PineconeConfig
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from pinecone import Pinecone
from src.embeddings.embedding_generator_interface import EmbeddingGenerator
from typing import List
import uuid

class PineconeRepository(SearchRepository):
    def __init__(self, config: PineconeConfig, embeddings: EmbeddingGenerator):
        self.pinecone = Pinecone(
            api_key=config.api_key,
        )
        self._index(config)
        index = self.pinecone.Index(config.index_name)
        
        embedding_fucntion = embeddings.get_embedding_client().get("client")
        self.vector_store = PineconeVectorStore(
            index=index,
            embedding_function=embedding_fucntion
        )
        
    
    def _index(self, config: PineconeConfig) -> None:
        """Create Index in the search backend."""
        if not self.pinecone.has_index(config.index_name):
            self.pinecone.create_index(
                name=config.index_name,
                dimension=1536,
                metric="cosine",
                vector_type="dense"
            )
            
    async def add_documents(self, docs: List[Document], ids: List[uuid.UUID]) -> None:
        self.vector_store.aadd_documents(documents=docs, ids=ids)
        
    def search(self, query, top_k: int = 5) -> list[Document]:
        return self.vector_store.similarity_search(query, k=top_k)