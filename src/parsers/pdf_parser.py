from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
import os
from parsers.pdfparser_interface import PDFParser
from langchain_openai import ChatOpenAI
from conifg import OpenAIChatConfig
import fitz, base64
from langchain.schema import HumanMessage

class PDFParserImpl(PDFParser):
    def __init__(self, file_path: str, config: OpenAIChatConfig):
        self.file_path = file_path
        self.llm = ChatOpenAI(
            model=config.model_name,
            max_retries=config.max_retries,
            api_key=config.api_key,
            base_url=config.endpoint
        )

    def parse(self, file_path: str) -> List[Document]:
        """Parse PDF and return list of documents."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        loader = PyMuPDFLoader(
            file_path,  
            extract_tables='html',
        )
        documents = loader.load() + self.parse_images(file_path)
        print(f"Parsed {len(documents)} documents from {file_path}: {documents}")
        return documents
    
    def parse_images(self, file_path: str) -> List[Document]:
        """Extract and parse images from PDF."""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        doc = fitz.open(file_path)
        image_docs = []
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            image_list = page.get_images(full=True)
            
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                
                image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                
                message = HumanMessage(
                    content=[
                        {"type": "text", "text": "Give the image content text?"},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                        },
                    ],
                )
                
                response = self.llm.invoke([message])  # Example of using LLM with image bytes
                
                image_doc = Document(
                    page_content=response.content,
                    metadata={
                        "page_number": page_num + 1,
                        "image_index": img_index + 1,
                        "image_extension": image_ext,
                        "source": file_path
                    }
                )
                image_docs.append(image_doc)
        
        print(f"Extracted {len(image_docs)} images from {file_path}")
        return image_docs
    
    def split_documents(self, documents: List[Document]) -> List[Document]:
        """Split documents into smaller chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=100,
            chunk_overlap=10,
            length_function=len,
        )
        split_docs = text_splitter.split_documents(documents)
        return split_docs