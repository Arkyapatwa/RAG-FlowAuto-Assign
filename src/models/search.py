from pydantic import BaseModel, Field
from typing import Optional
from typing import List
from langchain_core.documents import Document

class SearchRequestModel(BaseModel):
    query: str
    file_name: Optional[str] = Field(None, description="File name")
    top_k: Optional[int] = Field(5, description="top k docs")
    
class SearchResponseModel(BaseModel):
    related_documents: List[Document]
    answer: Optional[str]