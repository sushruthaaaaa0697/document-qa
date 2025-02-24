import unittest
import requests


class TestDocumentUpload(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8080/query/user-query/'
        self.headers = {'Content-Type': 'application/json'}

    def test_user_query(self):
        data = {
            "client_id": "4da8a172-8d9e-418f-ba69-773a375e8f25",
            "query": "According to the document, what is main cause for global warming? "
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_method_not_allowed(self):
        data = {
            "client_id": "0f869ba1-b59f-4ba7-9b78-521c4a4b97ff",
            "query": "According to the document, what is main cause for global warming? "
        }
        response = requests.get(self.url, data=data)
        self.assertEqual(response.status_code, 405)

    def test_unprocessed_entity(self):
        data = {
            "id": "0f869ba1-b59f-4ba7-9b78-521c4a4b97ff",
            "query": "According to the document, what is main cause for global warming? "
        }
        response = requests.get(self.url, data=data)
        self.assertEqual(response.status_code, 405)


if __name__ == '__main__':
    unittest.main()
