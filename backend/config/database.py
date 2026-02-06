from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os 
from typing import Optional

class Database:
    client: Optional[AsyncIOMotorClient] = None

    @classmethod 
    def get_client(cls) -> AsyncIOMotorClient:
        """Get async MongoDB client"""
        if cls.client is None:
            mongodb_uri = os.getenv("MONGODB_URI")
            if not mongodb_uri:
                raise ValueError("MONGODB_URI not found in environment variables")
            cls.client = AsyncIOMotorClient(mongodb_uri)
            return cls.client
        
    @classmethod
    def get_database(cls):
        """Get database instance"""
        client= cls.get_client()
        db_name= os.getenv("DATABASE_NAME", "custom_ai_assistant")
        return client[db_name]
        # why i store name in database ? 
    
    @classmethod
    async def close_client(cls):
        """close MongoDB client"""
        if cls.client:
            cls.client.close()
            cls.client = None
    
def get_db():
   
    return Database.get_database()