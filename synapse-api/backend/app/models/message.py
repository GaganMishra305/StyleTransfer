from pydantic import BaseModel

class Message(BaseModel):
    role : str
    text : str