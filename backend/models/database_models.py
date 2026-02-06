from pydantic import  BaseModel , Field
from typing import List , Optional
from datetime import datetime
from bson import ObjectId

class pyObjectId (ObjectId):
    """Custom ObjectId type for Pydantic """
    @classmethod 
    def __get_validators__(cls):
        yield cls.validate 
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type = "string")


class Message(BaseModel):
    """Single Message in a conversation """
    role: str
    content : str 
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
class Conversation(BaseModel):
    """Conversation document for MongoDB """
    id: Optional[pyObjectId ] = Field(alias= "_id", default = None)
    conversation_id : str 
    title: Optional[str] = None
    message: List[Message]=[]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
         arbitrary_types_allowed = True
         json_encoders = {ObjectId: str}
         populate_by_name = True