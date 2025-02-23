from docling.datamodel.base_models import InputFormat
from docling.document_converter import DocumentConverter
from .base_factory import Reader
import logging


class DocumentReader(Reader):
    """
    A DocumentReader class for reading and converting documents from various formats into Markdown.

    This class is a specialized reader that handles the conversion of documents from supported formats
    into Markdown using an asynchronous method. It leverages the DocumentConverter class to perform
    the conversion process.

    Attributes:
        path (str): The file path of the document to be read and converted.

    Methods:
        __init__(self, path): Initializes the DocumentReader instance with a specific document path.
        read(self): Asynchronously reads and converts the specified document to Markdown format.
    """

    def __init__(self, path):
        """
        Initializes a new instance of the DocumentReader class with a specified path for the document.

        This constructor logs an informational message indicating that the DocumentReader has been
        initialized with the provided path. This is helpful for debugging and tracking the document
        path being processed.

        Args:
            path (str): The file path of the document to be read and converted.
        """
        self.path = path
        logging.info(f"DocumentReader initialized with path: {self.path}")

    async def read(self):
        """
        Asynchronously reads and converts the document from the specified path to Markdown format.

        This method uses the DocumentConverter class to convert the document from supported input formats
        (PDF, IMAGE, DOCX, HTML, PPTX) to Markdown. The conversion result is logged as successful upon
        completion.

        Returns:
            str: The converted document in Markdown format.

        Raises:
            ConversionError: If the document conversion fails.
        """
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

