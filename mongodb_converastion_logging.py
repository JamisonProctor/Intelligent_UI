from pymongo import MongoClient
from datetime import datetime
import uuid
import streamlit as st  

server_url = st.secrets["SERVER_URL"]

# Helper function to get connect to the correct collection in database
def get_conversations_collection():
    client = MongoClient(server_url)
    db = client.intelligent_ui
    return db.conversations

# Initialize a new conversation document. Returns the conversation id.
def initialize_conversation(model_name):
    conversations = get_conversations_collection()
    conversation_id = str(uuid.uuid4())
    initialized_conversation = {
        '_id' : conversation_id,
        'model_used' : model_name,
        'interactions' : []
    }
    conversations.insert_one(initialized_conversation)
    return conversation_id

# Update conversation document with a new interaction 
def update_conversation(conversation_id, query, response):
    conversations = get_conversations_collection()
    new_interaction = {
        'query' : query,
        'response' : response,
        'timestamp' : datetime.now().isoformat()
    }

    conversations.update_one(  
        { '_id' : conversation_id },
        { '$push' : { 'interactions' : new_interaction } }
    )

# Helper function to print the conversation history
def check_conversation(conversation_id):
    conversations = get_conversations_collection()
    
    # Query the database to find the conversation with the given ID
    conversation = conversations.find_one({'_id': conversation_id})
    
    # Check if the conversation exists
    if conversation:
        print(f"Conversation ID: {conversation_id}")
        print("=" * 50)
        
        for i, interaction in enumerate(conversation['interactions'], 1):
            print(f"Interaction #{i}")
            print(f"User: {interaction['query']}")
            print(f"Chatbot: {interaction['response']}")
            print(f"Timestamp: {interaction['timestamp']}")
            print("-" * 50)
            
    else:
        print(f"No conversation found with ID: {conversation_id}")

    