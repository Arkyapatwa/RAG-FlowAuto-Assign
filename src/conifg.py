from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()

WATCHED_DIRECTORY = os.getenv("WATCHED_DIRECTORY", "./src/data")

class OpenAIEmbeddingsConfig(BaseSettings):
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    model_name: str = os.getenv("OPENAI_MODEL_NAME")
    max_retries: int = int(os.getenv("OPENAI_MAX_RETRIES", "3"))
    endpoint: str = os.getenv("OPENAI_ENDPOINT")

class OpenAIChatConfig(BaseSettings):
    api_key: str = os.getenv("OPENAI_API_KEY")
    model_name: str = os.getenv("OPENAI_CHAT_MODEL_NAME")
    temperature: float = float(os.getenv("OPENAI_CHAT_TEMPERATURE", "0.7"))
    max_retries: int = int(os.getenv("OPENAI_CHAT_MAX_RETRIES", "3"))
    endpoint: str = os.getenv("OPENAI_ENDPOINT")
    
class PineconeConfig(BaseSettings):
    api_key: str = os.getenv("PINECONE_API_KEY")
    index_name: str = os.getenv("PINECONE_INDEX_NAME")
    namespace: str = os.getenv("PINECONE_NAMESPACE")
