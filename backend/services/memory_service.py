from typing import List, Dict
import uuid

class MemoryService:
    """
    Simple in-memory storage for chat history.
    Later, you'll replace this with MongoDB.
    """
    
    def __init__(self):
        # Dictionary to store conversations
        # Key: conversation_id, Value: list of messages
        self.conversations: Dict[str, List[Dict[str, str]]] = {}
    
    def create_conversation(self) -> str:
        """Create new conversation and return ID"""
        conversation_id = str(uuid.uuid4())
        self.conversations[conversation_id] = []
        return conversation_id
    
    def add_message(self, conversation_id: str, role: str, content: str):
        """Add message to conversation history"""
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = []
        
        self.conversations[conversation_id].append({
            "role": role,
            "content": content
        })
    
    def get_conversation(self, conversation_id: str, last_n: int = 10) -> List[Dict[str, str]]:
        """
        Get conversation history
        
        Args:
            conversation_id: Which conversation
            last_n: Return only last N messages (keeps context window small)
        
        Returns:
            List of messages
        """
        if conversation_id not in self.conversations:
            return []
        
        return self.conversations[conversation_id][-last_n:]