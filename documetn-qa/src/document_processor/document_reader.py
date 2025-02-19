from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from .base_factory import Reader
import logging

class DocumentReader(Reader):
    def __init__(self, path):
        self.path = path
        logging.info(f"DocumentReader initialized with path: {self.path}")

    def read(self):
        doc_converter = DocumentConverter(
            allowed_formats=[
                InputFormat.PDF,
                InputFormat.IMAGE,
                InputFormat.DOCX,
                InputFormat.HTML,
                InputFormat.PPTX,
            ]
        )
        result = doc_converter.convert(self.path)
        logging.info("Document conversion successful")
        return result.document.export_to_markdown()
