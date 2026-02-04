from pydantic  import BaseModel
from typing import List, Optional

class ChatMessage(BaseModel):
    role: str
    content: str
    
class ChatRequest(BaseModel):
    message: str
    mode: Optional[str] = "default"
    conversation_id: Optional[str] = None



class ChatResponse(BaseModel):
     response :str
     conversation_id: str