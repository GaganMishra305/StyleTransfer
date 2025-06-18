from fastapi import FastAPI
from app.llm.groq_client import GroqClient
from app.models.message import Message
app = FastAPI()

@app.get("/")
async def health_check():
    return {
        "status": "healthy"
    }
