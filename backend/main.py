# CRITICAL: Load environment variables FIRST
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
from pathlib import Path

# Add backend directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from models.schemas import ChatRequest, ChatResponse
from services.ai_service import AIService
from services.memory_service import MemoryService

# Initialize FastAPI app
app = FastAPI(
    title="Custom AI Assistant",
    description="Modular AI assistant with configurable modes",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
ai_service = AIService()
memory_service = MemoryService()

@app.get("/")
def read_root():
    """Health check endpoint"""
    return {"status": "healthy", "message": "Custom AI Assistant is running!"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """Main chat endpoint"""
    try:
        # Create or get conversation
        conversation_id = request.conversation_id
        if not conversation_id:
            conversation_id = memory_service.create_conversation()
        
        # Add user message to history
        memory_service.add_message(conversation_id, "user", request.message)
        
        # Get conversation history
        history = memory_service.get_conversation(conversation_id)
        
        # Generate AI response
        ai_response = ai_service.generate_response(history, request.mode)
        
        # Save AI response to history
        memory_service.add_message(conversation_id, "assistant", ai_response)
        
        return ChatResponse(
            response=ai_response,
            conversation_id=conversation_id
        )
    
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