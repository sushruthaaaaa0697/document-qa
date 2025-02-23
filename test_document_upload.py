import unittest
import requests


class TestDocumentUpload(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/document/upload-document/'
        self.headers = {'Content-Type': 'multipart/form-data'}

    def test_upload_document(self):
        # Simulating file upload; in practice, open an actual file
        with open(r"C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf", "rb") as file:
            files = {
                'file': (r'C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf', file, 'application/pdf')
            }
            data = {
                'client_id': '5aa3375c-09d7-47e4-baed-044266a2f2a7',
                'document_type': 'document'
            }
            response = requests.post(self.url, files=files, data=data)
            self.assertEqual(response.status_code, 200)

    def test_method_not_allowed(self):
        # Simulating file upload; in practice, open an actual file
        with open(r"samples/jkt_doc_1.png", "rb") as file:
            files = {
                'file': (r'samples/jkt_doc_1.png', file, 'image/png')
            }
            data = {
                'client_id': '5aa3375c-09d7-47e4-baed-044266a2f2a7',
                'document_type': 'document'
            }
            response = requests.get(self.url, files=files, data=data)
            self.assertEqual(response.status_code, 405)

    def test_unprocessed_entity(self):
        # Simulating file upload; in practice, open an actual file
        with open(r"samples/jkt_doc_1.png", "rb") as file:
            files = {
                'file': (r'samples/jkt_doc_1.png', file, 'image/png')
            }
            data = {
                'id': '5aa3375c-09d7-47e4-baed-044266a2f2a7',
                'document_type': 'document'
            }
            response = requests.get(self.url, files=files, data=data)
            self.assertEqual(response.status_code, 405)

    def test_internal_server_error(self):
        # Simulating file upload; in practice, open an actual file
        with open(r"C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf", "rb") as file:
            files = {
                'file': (r'C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf', file, 'application/pdf')
            }
            data = {
                'client_id': '5aa3375c-09d7-47e4-baed-044266a2f2a7',
                'document_type': 'drivers_license'
            }
            response = requests.post(self.url, files=files, data=data)
            self.assertEqual(response.status_code, 500)


if __name__ == '__main__':
    unittest.main()
