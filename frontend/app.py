import streamlit as st
import requests
import json
from typing import Optional, List, Dict
from datetime import datetime

# Configuration
API_BASE_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="Custom AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

if "mode" not in st.session_state:
    st.session_state.mode = "default"

if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

if "all_conversations" not in st.session_state:
    st.session_state.all_conversations = []

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

def get_all_conversations():
    """Fetch all conversations from backend"""
    try:
        response = requests.get(f"{API_BASE_URL}/conversation")
        if response.status_code == 200:
            return response.json()["conversations"]
        return []
    except:
        return []

def get_conversation_detail(conversation_id: str):
    """Fetch full conversation detail"""
    try:
        response = requests.get(f"{API_BASE_URL}/conversation/{conversation_id}")
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def delete_conversation(conversation_id: str):
    """Delete a conversation"""
    try:
        response = requests.delete(f"{API_BASE_URL}/conversation/{conversation_id}")
        return response.status_code == 200
    except:
        return False

def load_conversation(conversation_id: str):
    """Load a conversation into the chat"""
    detail = get_conversation_detail(conversation_id)
    if detail:
        st.session_state.conversation_id = conversation_id
        st.session_state.mode = detail.get("mode", "default")
        st.session_state.messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in detail.get("messages", [])
        ]
        return True
    return False

def clear_conversation():
    """Clear conversation history"""
    st.session_state.conversation_id = None
    st.session_state.messages = []

def export_conversation_json(conversation_id: str):
    """Export conversation as JSON"""
    detail = get_conversation_detail(conversation_id)
    if detail:
        return json.dumps(detail, indent=2)
    return None

def export_conversation_text(conversation_id: str):
    """Export conversation as plain text"""
    detail = get_conversation_detail(conversation_id)
    if not detail:
        return None
    
    lines = [
        f"Conversation: {detail.get('title', 'Untitled')}",
        f"Mode: {detail.get('mode', 'default')}",
        f"Created: {detail.get('created_at', 'N/A')}",
        f"Updated: {detail.get('updated_at', 'N/A')}",
        "-" * 50,
        ""
    ]
    
    for msg in detail.get("messages", []):
        role = msg["role"].upper()
        content = msg["content"]
        timestamp = msg.get("timestamp", "")
        lines.append(f"[{role}] {timestamp}")
        lines.append(content)
        lines.append("")
    
    return "\n".join(lines)

def search_conversations(query: str, conversations: List[Dict]):
    """Search conversations by title or content"""
    if not query:
        return conversations
    
    query_lower = query.lower()
    filtered = []
    
    for conv in conversations:
        # Search in title
        if query_lower in conv.get("title", "").lower():
            filtered.append(conv)
            continue
        
        # Search in messages (need to fetch detail)
        detail = get_conversation_detail(conv["conversation_id"])
        if detail:
            for msg in detail.get("messages", []):
                if query_lower in msg["content"].lower():
                    filtered.append(conv)
                    break
    
    return filtered

# Custom CSS
st.markdown("""
<style>
    .conversation-item {
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        background-color: #f0f2f6;
        cursor: pointer;
    }
    .conversation-item:hover {
        background-color: #e0e2e6;
    }
    .active-conversation {
        background-color: #d0d2d6;
        border-left: 3px solid #ff4b4b;
    }
    .stat-box {
        padding: 15px;
        border-radius: 5px;
        background-color: #f0f2f6;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Mode selector
    available_modes = get_available_modes()
    mode_descriptions = {
        "default": "Helpful and friendly general assistant",
        "mentor": "Guides you through problems with questions",
        "exam": "Helps with exam preparation and explanations"
    }
    
    selected_mode = st.selectbox(
        "AI Mode",
        available_modes,
        index=available_modes.index(st.session_state.mode),
        help="Select the AI personality mode"
    )
    
    if selected_mode in mode_descriptions:
        st.info(mode_descriptions[selected_mode])
    
    if selected_mode != st.session_state.mode:
        st.session_state.mode = selected_mode
    
    st.divider()
    
    # New conversation button
    if st.button("➕ New Conversation", use_container_width=True):
        clear_conversation()
        st.rerun()
    
    st.divider()
    
    # Current conversation info
    st.subheader("Current Chat")
    if st.session_state.conversation_id:
        st.success("Active")
        st.caption(f"ID: {st.session_state.conversation_id[:8]}...")
        st.metric("Messages", len(st.session_state.messages))
    else:
        st.warning("No active conversation")
        st.metric("Messages", 0)
    
    st.divider()
    
    # Backend status
    st.subheader("System Status")
    try:
        response = requests.get(f"{API_BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            st.success("✅ Backend Online")
            st.caption(f"Version: {data.get('version', 'N/A')}")
            st.caption(f"Database: {data.get('database', 'N/A')}")
        else:
            st.error("❌ Backend Error")
    except:
        st.error("❌ Backend Offline")
    
    st.caption(f"API: {API_BASE_URL}")

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Header
    st.title("Custom AI Assistant")
    st.caption("Powered by Grok AI with MongoDB persistence")
    
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
        
        # Refresh conversation list
        st.rerun()

with col2:
    st.header("📚 Conversations")
    
    # Search bar
    search_query = st.text_input("🔍 Search conversations", placeholder="Search by title or content...")
    
    # Refresh button
    if st.button("🔄 Refresh", use_container_width=True):
        st.session_state.all_conversations = get_all_conversations()
    
    # Load conversations
    if not st.session_state.all_conversations:
        st.session_state.all_conversations = get_all_conversations()
    
    # Filter conversations
    filtered_conversations = search_conversations(
        search_query, 
        st.session_state.all_conversations
    )
    
    st.caption(f"Found {len(filtered_conversations)} conversation(s)")
    
    st.divider()
    
    # Display conversations
    if filtered_conversations:
        for conv in filtered_conversations:
            conv_id = conv["conversation_id"]
            is_active = conv_id == st.session_state.conversation_id
            
            with st.container():
                col_a, col_b = st.columns([4, 1])
                
                with col_a:
                    # Conversation title
                    title = conv.get("title", "Untitled")
                    if len(title) > 40:
                        title = title[:40] + "..."
                    
                    if st.button(
                        f"{'🟢' if is_active else '💬'} {title}",
                        key=f"load_{conv_id}",
                        use_container_width=True
                    ):
                        if load_conversation(conv_id):
                            st.rerun()
                    
                    # Metadata
                    st.caption(
                        f"Mode: {conv.get('mode', 'N/A')} | "
                        f"Messages: {conv.get('message_count', 0)} | "
                        f"Updated: {conv.get('updated_at', 'N/A')[:10]}"
                    )
                
                with col_b:
                    # Export menu
                    with st.popover("⋮"):
                        st.write("Actions")
                        
                        # Export JSON
                        json_data = export_conversation_json(conv_id)
                        if json_data:
                            st.download_button(
                                "📥 JSON",
                                json_data,
                                file_name=f"conversation_{conv_id[:8]}.json",
                                mime="application/json",
                                use_container_width=True
                            )
                        
                        # Export Text
                        text_data = export_conversation_text(conv_id)
                        if text_data:
                            st.download_button(
                                "📄 Text",
                                text_data,
                                file_name=f"conversation_{conv_id[:8]}.txt",
                                mime="text/plain",
                                use_container_width=True
                            )
                        
                        st.divider()
                        
                        # Delete
                        if st.button("🗑️ Delete", key=f"del_{conv_id}", use_container_width=True):
                            if delete_conversation(conv_id):
                                st.success("Deleted!")
                                if conv_id == st.session_state.conversation_id:
                                    clear_conversation()
                                st.session_state.all_conversations = get_all_conversations()
                                st.rerun()
                            else:
                                st.error("Failed to delete")
                
                st.divider()
    else:
        st.info("No conversations yet. Start chatting to create one!")

