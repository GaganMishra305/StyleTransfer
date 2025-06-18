import pytest
from backend.app.llm.groq_client import GeminiClient

@pytest.mark.asyncio
async def test_gemini_client():
    client = GeminiClient()
    response = await client.generate("Hello, how are you?")
    assert isinstance(response, str)
    assert len(response) > 0

