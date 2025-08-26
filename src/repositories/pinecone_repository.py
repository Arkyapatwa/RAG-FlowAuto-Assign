from repositories.search_repository_interface import SearchRepository
from conifg import PineconeConfig
from langchain_pinecone import PineconeVectorStore
from langchain_core.documents import Document
from pinecone import Pinecone, ServerlessSpec
from embeddings.embedding_generator_interface import EmbeddingGenerator
from typing import List
import uuid

class PineconeRepository(SearchRepository):
    def __init__(self, config: PineconeConfig, embeddings: EmbeddingGenerator):
        self.pinecone = Pinecone(
            api_key=config.api_key,
        )
        self.config = config
        self._index(config)
        index = self.pinecone.Index(config.index_name)
        
        embedding_fucntion = embeddings.get_embedding_client().get("client")
        self.vector_store = PineconeVectorStore(
            pinecone_api_key=config.api_key,
            index=index,
            embedding=embedding_fucntion,
            namespace=config.namespace
        )
        
    
    def _index(self, config: PineconeConfig) -> None:
        """Create Index in the search backend."""
        if not self.pinecone.has_index(config.index_name):
            self.pinecone.create_index(
                name=config.index_name,
                dimension=2000,
                metric="cosine",
                vector_type="dense",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )
            
    async def add_documents(self, docs: List[Document], ids: List[str | uuid.UUID]) -> None:
        await self.vector_store.aadd_documents(documents=docs, ids=ids)
        
    def search(self, query, top_k: int = 5) -> list[Document]:
        res = self.vector_store.similarity_search(query, k=top_k, namespace=self.config.namespace)
        print("fetched data: ", res)
        return res