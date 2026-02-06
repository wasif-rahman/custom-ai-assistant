from typing import List, Dict,Optional
from datetime import datetime
import uuid
from config.database import get_db
from models.database_models import Conversation, Message

class MemoryService:
    
    """MongoDB-backend conversation storage.
    Replaces in-memory dictionary with persistent database.
    """

    def __init__(self):
        self.db = get_db()
        self.collection =self.db.conversations


    async def create_conversation(self, mode: str = "default") -> str:
        """Create new conversation and return its ID"""
        conversation_id = str(uuid.uuid4())

        conversation = {
            "conversation_id": conversation_id,
            "title": None,
            "mode": mode,
            "messages": [],
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        await self.collection.insert_one(conversation)
        return conversation_id
    
    async def add_message(self, conversation_id: str, role: str, content: str):
        """Add message to conversation"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.utcno
        }
        
        # Update messages array and updated_at timestamp
        result = await self.collection.update_one(
            {"conversation_id": conversation_id},
            {
                "$push": {"messages": message},
                "$set": {"updated_at": datetime.utcnow()}
            }
        )


        # if convo doesn't exist
        if result.matched_count ==0:
            await self.create_conversation()
            await self.add_message(conversation_id,role,content)

        
        # Auto generate conversation name
        await self._update_title_if_needed(conversation_id,content,role)


        async def _update_title_if_needed(self,conversation_id:str, content : str , role :str ):
            """Generate conversation title based on first user message"""
        if role == "user":
            conversation = await self.collection.find_one({"conversation_id": conversation_id})
            if conversation and not conversation.get("title"):
                title = content[:50] + ("... "if len(content)>50 else"")
                await self.collection.update_one(
                    {"conversation_id":conversation_id},
                    {"$set":{"title" : title}}
                )
        async def get_convesation(self, conversation_id:str, last_n: int=10) -> List[Dict[str,str]]:
            """Get conversation history
             Args:
              conversation_id :which conversation 
              Returns: 
              List of messages (role + content onlly  without timestamps)
              """
            conversation = await self.collection.find_one({"conversation_id": conversation_id})
        
            if not conversation:
                return[]
            messages = conversation.get("messages",[])
            recent_messages = messages[-last_n:] if len(messages) > last_n else messages
        
        # Return in format expected by AI service (without timestamps)
            return [
                 {"role": msg["role"], "content": msg["content"]}
                for msg in recent_messages
              ]
    
    async def get_all_conversations(self, limit: int = 50) -> List[Dict]:
        """
        Get list of all conversations

        Returns:
            List of conversation summaries (id, title, message count, etc.)
        """
        cursor = self.collection.find().sort("updated_at", -1).limit(limit)
        conversations = await cursor.to_list(length=limit)
        
        return [
            {
                "conversation_id": conv["conversation_id"],
                "title": conv.get("title", "Untitled"),
                "mode": conv.get("mode", "default"),
                "message_count": len(conv.get("messages", [])),
                "created_at": conv["created_at"].isoformat(),
                "updated_at": conv["updated_at"].isoformat()
            }
            for conv in conversations
        ]
    
    async def get_conversation_detail(self, conversation_id: str) -> Optional[Dict]:
        """Get full conversation with all messages"""
        conversation = await self.collection.find_one({"conversation_id": conversation_id})
        
        if not conversation:
            return None
        
        return {
            "conversation_id": conversation["conversation_id"],
            "title": conversation.get("title", "Untitled"),
            "mode": conversation.get("mode", "default"),
            "messages": [
                {
                    "role": msg["role"],
                    "content": msg["content"],
                    "timestamp": msg["timestamp"].isoformat()
                }
                for msg in conversation.get("messages", [])
            ],
            "created_at": conversation["created_at"].isoformat(),
            "updated_at": conversation["updated_at"].isoformat()
        }
    
    async def delete_conversation(self, conversation_id: str) -> bool:
        """Delete a conversation"""
        result = await self.collection.delete_one({"conversation_id": conversation_id})
        return result.deleted_count > 0
    
    async def update_conversation_mode(self, conversation_id: str, mode: str) -> bool:
        """Update conversation mode"""
        result = await self.collection.update_one(
            {"conversation_id": conversation_id},
            {"$set": {"mode": mode, "updated_at": datetime.utcnow()}}
        )
        return result.modified_count > 0
            




























         
    