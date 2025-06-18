import os
from typing import List
from groq import Groq, AsyncGroq
from dotenv import load_dotenv
from app.llm.base import BaseLLMClient
from app.config.config import Config
from app.models.message import Message

env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(env_path)

# api key
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# configuration
text_config = Config.get_model_config('text')
image_config = Config.get_model_config('image')
audio_config = Config.get_model_config('audio')

# Main class
class GroqClient(BaseLLMClient):
    def  __init__(self):
        self.client = Groq(api_key = GROQ_API_KEY)
        self.async_client = AsyncGroq(api_key = GROQ_API_KEY)
        
    def generate_text(self, messages: List[Message], generation_config=None):
        # Convert Message objects to dict format
        message_dicts = [msg.to_dict() for msg in messages]
        
        chat_completion = self.client.chat.completions.create(
            messages=message_dicts,
            model=text_config['model_name'],
            temperature=text_config['temperature'],
            max_tokens=text_config['max_tokens'],
            top_p=text_config['top_p'],
            stream=False
        )
        return chat_completion.choices[0].message.content
    
    def generate_text_stream(self, messages):
        chat_completion = self.async_client.chat.completions.create(
            messages=messages,
            model=text_config['model_name'],
            temperature=text_config['temperature'],
            max_completion_tokens=text_config['max_tokens'],
            top_p=text_config['top_p'],
            stop=None if text_config['stop'] == "None" else text_config['stop'],
            stream=text_config['stream'] == "True",
        )
        return chat_completion.choices[0].message.content

    def generate_image():
        pass
    
    def  generate_tts():
        pass