from .document_reader import DocumentReader
import logging

class AdapterFactory:

    @staticmethod
    def get_adapter(adapter_type: str):
        logging.info(f"Fetching adapter for type: {adapter_type}")
        adapter_map = {
            "document": DocumentReader
        }
        adapter = adapter_map.get(adapter_type)
        if adapter:
            logging.info(f"Adapter found: {adapter.__name__}")
        else:
            logging.warning(f"No adapter found for type: {adapter_type}")
        return adapter
