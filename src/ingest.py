import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pipelines.etl_pipeline_interface import ETLPipeline
from conifg import WATCHED_DIRECTORY
import asyncio

from pipelines.pdf_rag_etl_pipeline import PDFRAGETLPipeline
from parsers.pdf_parser import PDFParserImpl
from repositories.pinecone_repository import PineconeRepository
from embeddings.openai_embeddings import OpenAIEmbeddingsGenerator
from conifg import OpenAIEmbeddingsConfig, PineconeConfig, OpenAIChatConfig

class PDFHandler(FileSystemEventHandler):
    def __init__(self, etl_pipeline: ETLPipeline):
        self.etl_pipeline = etl_pipeline

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.pdf'):
            print(f"New PDF detected: {event.src_path}")
            print("Starting ETL process...")
            asyncio.run(self.etl_pipeline.run(file_path=event.src_path.replace("\\", "/")))
            print("ETL process completed.")
            
if __name__ == "__main__":

    # Initialize components
    parser = PDFParserImpl(file_path="", config=OpenAIChatConfig())  # file_path will be set dynamically
    embeddings = OpenAIEmbeddingsGenerator(config=OpenAIEmbeddingsConfig())
    repository = PineconeRepository(config=PineconeConfig(), embeddings=embeddings)  # embeddings will be set later
    etl_pipeline = PDFRAGETLPipeline(parser, repository, embeddings)

    event_handler = PDFHandler(etl_pipeline)
    observer = Observer()
    observer.schedule(event_handler, path=WATCHED_DIRECTORY, recursive=False)
    
    print(f"Watching directory: {WATCHED_DIRECTORY} for new PDF files...")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()