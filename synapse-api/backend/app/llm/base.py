from abc import ABC, abstractmethod
from typing import List

from app.models.message import Message


class BaseLLMClient(ABC):
    @abstractmethod
    async def generate_text(self, messages: List[Message]) -> str:
        pass

    @abstractmethod
    async def generate_text_stream(self, messages: List[Message]):
        pass

    @abstractmethod
    async def generate_image():
        pass

    @abstractmethod
    async def generate_tts():
        pass