import os
import logging
from mistralai import Mistral
from fastapi import HTTPException

logging.basicConfig(level=logging.INFO)

api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

def generate_ai_tagline(title: str, author: str, description: str) -> str:
    try:
        prompt = (
            f"Write a short, engaging tagline for the book titled '{title}' "
            f"written by {author}. Description: {description} and give the response in as paragraph"
        )
        
        chat_response = client.chat.complete(
            model="mistral-large-latest",  # Model name
            messages=[{"role": "user", "content": prompt}]
        )
        
        ai_tagline = chat_response.choices[0].message.content
        return ai_tagline

    except Exception as e:
        logging.error(f"AI service error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI service error: {str(e)}")
