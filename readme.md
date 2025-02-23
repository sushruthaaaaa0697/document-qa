Steps to run the application:
1. Download and install ollama
2. Install requirements using - pip install -r requirements.txt
3. Run python main.py
4. Open postman and paste the below endpoint to register the document
curl --location 'http://0.0.0.0:8080/document/upload-document/' \
--form 'client_id="a63d2840-da23-4f21-afc0-46285a0803a3"' \
--form 'document_type="document"' \
--form 'file=@"/C:/Users/SushrutaBhat/Downloads/s41598-024-83664-1.pdf"'
    
    The client_id should be unique as this endpoint registers the client. The client id and chunks of the document 
    along with their vectors are written to chromadb. During retrieval, only information related to that particular
    client is filtered and top_k results are passed to the LLM. 

5. Open postman and paste the below endpoint to ask queries on the document
 curl --location 'http://localhost:8080/query/user-query/' \
--data '{
    "client_id": "a63d2840-da23-4f21-afc0-46285a0803a3", 
    "query": "What are some opportunities for recovery of cost?"
}'
   
   This endpoint takes in the user's queries. The query of the user is internally converted to vector and a similarity 
   search is done to fetch the most similar chunks of the document to the user query. The user query and the chunks of 
    text is sent to the LLM. 

Sample documents to run are given in the /samples folder. Along with the sample documents, sample questions are also 
provided. This could help user to understand the kind of questions that can be asked to the model. 


Refer to docstrings in each class to understand what the class actually does. 

DocumentReader class reads the document and converts to mark down format.

TextChunker class converts the document into chunks. 

VectorStore class does two things. It writes the embeddings to chromadb (Vector database). The also has a method to load
the database, filter records based on client id and get the similar chunks. 


