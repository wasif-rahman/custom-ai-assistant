# CRITICAL: Load environment variables FIRST
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from models.schemas import ChatRequest, ChatResponse
from services.ai_service import AIService
from services.memory_service import MemoryService
from config.database import Database 


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("connecting to MongoDB....")
    # Motor handles async connections lazily, just verify variables exist
    mongodb_uri = os.getenv("MONGODB_URI")
    if not mongodb_uri:
        print("ERROR: MONGODB_URI not set in .env")
    else:
        print("MongoDB URI loaded successfully")
    print("connected to database successfully")
    
    yield
    print("Closing database connection")
    await Database.close()
    print("Database connection closed")
    

# Initialize FastAPI app
app = FastAPI(
    title="Custom AI Assistant",
    description="Modular AI assistant with configurable modes and persistent storage",
    version="2.0.0",
    lifespan=lifespan
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services (lazy loading - database only connects when first used)
ai_service = AIService()
memory_service = MemoryService()

@app.get("/")
def read_root():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Custom AI Assistant is running!",
        "version": "2.0.0",
        "database": "MongoDB"        
        
        }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        # Create or get conversation
        conversation_id = request.conversation_id
        if not conversation_id:
            conversation_id = await memory_service.create_conversation(request.mode)
        
        # Add user message to history
        await memory_service.add_message(conversation_id, "user", request.message)
        
        # Get conversation history
        history = await memory_service.get_conversation(conversation_id)
        
        # Generate AI response
        ai_response = ai_service.generate_response(history, request.mode)
        
        # Save AI response to history
        await memory_service.add_message(conversation_id, "assistant", ai_response)
        
        return ChatResponse(
            response=ai_response,
            conversation_id=conversation_id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/conversation")
async def list_conversation(limit: int = 50):
    """Get list of all the conversations"""
    try:
        conversations = await memory_service.get_all_conversations(limit)
        return {"conversations": conversations, "count": len(conversations)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/conversation/{conversation_id}")
async def get_conversation(conversation_id: str):
    """Get full conversation"""
    try:
        conversation = await memory_service.get_conversation_detail(conversation_id)
        if not conversation :
            raise HTTPException(status_code=404,detail="Conversation not found")
        return conversation
    except HTTPException:
        raise 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/conversation/{conversation_id}")
async def delete_conversation(conversation_id: str):
    """Delete a conversation"""
    try:
        success = await memory_service.delete_conversation(conversation_id)
        if not success:
            raise HTTPException(status_code=404, detail="Conversation not found")
        return {"message": "Conversation deleted successfully"}
    except HTTPException:
        raise 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/modes")
def get_modes():
    """Get available AI modes"""
    return {
        "modes": list(ai_service.prompts["system_prompts"].keys())
    }

@app.get("/debug/check-key")
def check_key():
    """Debug: Check if API key is loaded"""
    key = os.getenv("OPENAI_API_KEY")
    return {
        "key_loaded": key is not None,
        "key_starts_with": key[:10] if key else "NONE"
    }
    