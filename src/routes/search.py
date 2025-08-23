from fastapi import APIRouter, Depends
from services.search_service_interface import SearchService

def get_search_service() -> SearchService:
    return SearchService()

router = APIRouter()

@router.get("/search")
def search(query: str, top_k: int = 5, service: SearchService = Depends(get_search_service)):
    return service.search(query=query, top_k=top_k)