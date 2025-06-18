from typing import Any, Dict, Literal
from pydantic import BaseModel

Role = Literal["bot", "user", "tool", "system"]

class Message(BaseModel):
    role: Role
    content: str
    
    def to_dict(self) -> Dict[str, Any]:
        return {"role": self.role, "content": self.content}