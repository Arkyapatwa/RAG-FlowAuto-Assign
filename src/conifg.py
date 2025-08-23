from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()

class OpenAIEmbeddingsConfig(BaseSettings):
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    model_name: str = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
    temperature: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    max_retries: int = int(os.getenv("OPENAI_MAX_RETRIES", "3"))

class OpenAIChatConfig(BaseSettings):
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    model_name: str = os.getenv("OPENAI_CHAT_MODEL_NAME", "gpt-3.5-turbo")
    temperature: float = float(os.getenv("OPENAI_CHAT_TEMPERATURE", "0.7"))
    max_retries: int = int(os.getenv("OPENAI_CHAT_MAX_RETRIES", "3"))
    
class PineconeConfig(BaseSettings):
    api_key: str = os.getenv("PINECONE_API_KEY", "")
    environment: str = os.getenv("PINECONE_ENVIRONMENT", "")
    index_name: str = os.getenv("PINECONE_INDEX_NAME", "pdf-index")
