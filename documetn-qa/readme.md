Steps to run the application:
1. Download and install ollama
2. Install requirements using - pip install -r requirements.txt
3. Run python main.py
4. Open postman and run the below endpoint to register the document
curl --location 'http://0.0.0.0:8080/document/upload-document/' \
--form 'client_id="a63d2840-da23-4f21-afc0-46285a0803a3"' \
--form 'document_type="document"' \
--form 'file=@"/C:/Users/SushrutaBhat/Downloads/s41598-024-83664-1.pdf"'

5. Open postman and run the below endpoint to ask queries on the document
 curl --location 'http://localhost:8080/query/user-query/' \
--data '{
    "client_id": "a63d2840-da23-4f21-afc0-46285a0803a3", 
    "query": "What are some opportunities for recovery of cost?"
}'
