from fastapi import APIRouter, Depends
from services.search_service import SearchServiceImpl
from services.search_service_interface import SearchService
from repositories.pinecone_repository import PineconeRepository
from embeddings.openai_embeddings import OpenAIEmbeddingsGenerator
from models.search import SearchRequestModel, SearchResponseModel
from conifg import PineconeConfig, OpenAIEmbeddingsConfig

def get_search_service() -> SearchService:
    embeddings = OpenAIEmbeddingsGenerator(config=OpenAIEmbeddingsConfig())
    repository = PineconeRepository(config=PineconeConfig(), embeddings=embeddings)
    return SearchServiceImpl(repository=repository)

router = APIRouter(prefix="/pdf")

@router.post(
    "/ask",
    response_model=SearchResponseModel,
    summary="Search within a PDF",
)
def ask_pdf(searchRequest: SearchRequestModel, service: SearchService = Depends(get_search_service)) -> SearchResponseModel:
    return service.search(query=searchRequest.query, top_k=searchRequest.top_k)