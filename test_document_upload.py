import unittest
import requests


class TestDocumentUpload(unittest.TestCase):
    def setUp(self):
        self.url = 'http://0.0.0.0:8080/document/upload-document/'
        self.headers = {'Content-Type': 'multipart/form-data'}

    def test_upload_document(self):
        # Simulating file upload; in practice, open an actual file
        with open(r"C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf", "rb") as file:
            files = {
                'file': (r'C:\Users\SushrutaBhat\Downloads\jkt_doc_3.pdf', file, 'image/png')
            }
            data = {
                'client_id': '89940fef-4449-4973-912d-ee951da915cd',
                'document_type': 'document'
            }
            response = requests.post(self.url, files=files, data=data)
            self.assertEqual(response.status_code, 200)
            # Add more assertions here depending on the response structure
            # For example:
            # self.assertIn('success', response.json()['status'])

if __name__ == '__main__':
    unittest.main()
