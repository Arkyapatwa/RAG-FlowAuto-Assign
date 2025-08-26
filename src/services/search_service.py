from services.search_service_interface import SearchService
from repositories.search_repository_interface import SearchRepository
from models.search import SearchResponseModel
from langchain_core.documents import Document
from typing import List

class SearchServiceImpl(SearchService):
    def __init__(self, repository: SearchRepository):
        self.repository = repository
        
    def search(self, query: str, top_k: int = 5) -> SearchResponseModel:
        fetched_docs: List[Document] = self.repository.search(query=query, top_k=top_k)
        print(fetched_docs)
        searched_response = SearchResponseModel(
            related_documents=fetched_docs,
            answer=None
        )
        
        return searched_response