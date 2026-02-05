import streamlit as st
import requests
import json
from typing import Optional

# Configuration
API_BASE_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="Custom AI Assistant",
    page_icon="🐱‍👤",
    layout="centered"
)

# Initialize session state
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "default"

# Helper functions
def get_available_modes():
    """Fetch available AI modes from backend"""
    try:
        response = requests.get(f"{API_BASE_URL}/modes")
        if response.status_code == 200:
            return response.json()["modes"]
        return ["default", "mentor", "exam"]
    except:
        return ["default", "mentor", "exam"]

def send_message(message: str, mode: str, conversation_id: Optional[str] = None):
    """Send message to backend and get response"""
    try:
        payload = {
            "message": message,
            "mode": mode
        }
        
        if conversation_id:
            payload["conversation_id"] = conversation_id
        
        response = requests.post(
            f"{API_BASE_URL}/chat",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "response": f"Error: {response.status_code} - {response.text}",
                "conversation_id": conversation_id
            }
    except Exception as e:
        return {
            "response": f"Connection error: {str(e)}. Make sure backend is running on {API_BASE_URL}",
            "conversation_id": conversation_id
        }

def clear_conversation():
    """Clear conversation history"""
    st.session_state.conversation_id = None
    st.session_state.messages = []

# UI Layout
st.title("Custom AI Assistant")
st.caption("Modular AI assistant with configurable modes")

# Sidebar
with st.sidebar:
    st.header("Settings")
    
    # Mode selector
    available_modes = get_available_modes()
    mode_descriptions = {
        "default": "Helpful and friendly general assistant",
        "mentor": "Guides you through problems with questions",
        "exam": "Helps with exam preparation and explanations",
        "caring_girl": "A warm and empathetic friend"
    }
    
    selected_mode = st.selectbox(
        "AI Mode",
        available_modes,
        index=available_modes.index(st.session_state.mode) if st.session_state.mode in available_modes else 0,
        help="Select the AI personality mode"
    )
    
    # Show mode description
    if selected_mode in mode_descriptions:
        st.info(mode_descriptions[selected_mode])
    
    # Update mode if changed
    if selected_mode != st.session_state.mode:
        st.session_state.mode = selected_mode
    
    st.divider()
    
    # Conversation info
    if st.session_state.conversation_id:
        st.success("Conversation active")
        st.caption(f"ID: {st.session_state.conversation_id[:8]}...")
    else:
        st.warning("No active conversation")
    
    # Clear conversation button
    if st.button("New Conversation", use_container_width=True):
        clear_conversation()
        st.rerun()
    
    st.divider()
    
    # Stats
    st.metric("Messages", len(st.session_state.messages))
    
    st.divider()
    
    # Backend status
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            st.success("Backend: Online")
        else:
            st.error("Backend: Error")
    except:
        st.error("Backend: Offline")
    
    st.caption(f"API: {API_BASE_URL}")

# Main chat area
st.divider()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response_data = send_message(
                prompt, 
                st.session_state.mode,
                st.session_state.conversation_id
            )
            
            # Update conversation ID
            st.session_state.conversation_id = response_data["conversation_id"]
            
            # Display response
            ai_response = response_data["response"]
            st.markdown(ai_response)
    
    # Add assistant message to chat
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
