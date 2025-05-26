import os
from dotenv import load_dotenv
import chainlit as cl
from litellm import completion
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# System prompt for better responses
SYSTEM_PROMPT = {
    "role": "system", 
    "content": "You are PSQAsim, a helpful AI assistant. Provide clear, concise, and accurate responses."
}

@cl.on_chat_start
async def start():
    """Initialize chat session with welcome message."""
    # Set up session with system prompt
    cl.user_session.set("messages", [SYSTEM_PROMPT])
    
    # Welcome message with better styling
    welcome_msg = """
    # 🤖 Welcome to PSQAsim AI Assistant!
    
    I'm here to help you with any questions or tasks you have. Feel free to ask me anything!
    
    **What I can help with:**
    - Answering questions
    - Writing and editing
    - Problem solving
    - Code assistance
    - General conversation
    """
    
    await cl.Message(content=welcome_msg).send()

@cl.on_message
async def handle_message(message: cl.Message):
    """Process user messages and generate AI responses."""
    # Show typing indicator
    async with cl.Step(name="🧠 Thinking", type="run") as step:
        try:
            # Get conversation history
            messages = cl.user_session.get("messages", [SYSTEM_PROMPT])
            
            # Add user message
            messages.append({"role": "user", "content": message.content})
            
            # Get AI response
            response = completion(
                model="gemini/gemini-2.0-flash",
                api_key=GEMINI_API_KEY,
                messages=messages,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Add AI response to history
            messages.append({"role": "assistant", "content": ai_response})
            cl.user_session.set("messages", messages)
            
            step.output = "Response generated successfully!"
            
        except Exception as e:
            ai_response = f"⚠️ Sorry, I encountered an error: {str(e)}"
            step.output = f"Error: {str(e)}"
    
    # Send response
    await cl.Message(content=ai_response).send()

@cl.on_chat_end
async def save_chat():
    """Save chat history when session ends."""
    try:
        messages = cl.user_session.get("messages", [])
        
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"psqasim_chat_{timestamp}.json"
        
        # Save to file
        chat_data = {
            "timestamp": datetime.now().isoformat(),
            "messages": messages[1:]  # Skip system prompt
        }
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(chat_data, f, indent=2, ensure_ascii=False)
            
        print(f"💾 Chat saved to {filename}")
        
    except Exception as e:
        print(f"❌ Error saving chat: {e}")

# Optional: Add custom CSS for better UI
@cl.on_settings_update
async def setup_agent(settings):
    """Handle settings updates if needed."""
    pass