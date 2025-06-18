import pytest
from app.llm.groq_client import GroqClient
from app.models.message import Message

def test_groq_client():
    client = GroqClient()
    messages = [
        Message(role="system",  content="Your name is LLAMA."),
        Message(role="user", content="What is your name?")
    ]
    
    response = client.generate_text(messages=messages)
    assert isinstance(response, str)
    assert len(response) > 0