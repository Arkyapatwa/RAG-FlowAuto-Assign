from pydantic import BaseModel
from typing import Optional

class SearchRequestModel(BaseModel):
    query: str
    file_name: Optional[str] = None
    
class SearchResponseModel(BaseModel):
    results: str