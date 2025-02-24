import ollama
import logging


async def answer(text):
    logging.info("Sending text to Ollama for processing.")

    response = ollama.chat(
        model="deepseek-r1:1.5b",
        messages=[
            {"role": "user", "content": text},
        ],
    )
    logging.info("Received response from Ollama.")
    return response["message"]["content"]


def prompt_builder(text, user_query):
    logging.info("Building prompt for query processing.")
    prompt = f"""
    Given to you is the text inside a document. 
    {text}

    Using the information in the text, answer precisely to the questions given to you.
    {user_query}
    
    If there is no text from the document, please reply back politely saying you cannot answer this question now
"""
    logging.info("Prompt successfully constructed.")
    return prompt
