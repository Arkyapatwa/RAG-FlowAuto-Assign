from pydantic import BaseModel
from typing import Optional

class SearchRequestModel(BaseModel):
    query: str
    file_name: Optional[str] = None
    top_k: Optional[int] = 5
    
class SearchResponseModel(BaseModel):
    results: str