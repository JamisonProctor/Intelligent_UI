from pymongo import MongoClient
from datetime import datetime
import streamlit as st  

server_url = st.secrets["SERVER_URL"]
collection_name = 'conversations_jamison'

# Helper function to get connect to the correct collection in database
def connect_mongodb_collection(server_url = server_url, collection_name = collection_name):
    client = MongoClient(server_url)
    db = client.intelligent_ui
    return db[f"{collection_name}"]

# Initialize a new conversation document. Returns the conversation id.
def initialize_mongodb_conversation(model_name, collection_name=collection_name):
    conversations = connect_mongodb_collection() 
    initialized_conversation = {
        'model_used' : model_name,
        'timestamp' : datetime.now().isoformat(),
        'interactions' : []
    }
    conversation_id = conversations.insert_one(initialized_conversation).inserted_id
    return conversation_id

# Update conversation document with a new interaction 
def update_mongodb_conversation(conversation_id, query, response, collection_name=collection_name):
    conversations = connect_mongodb_collection()
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
def check_mongodb_conversation(conversation_id, collection_name=collection_name):
    conversations = connect_mongodb_collection()
    
    # Query the database to find the conversation with the given ID
    conversation = conversations.find_one({'_id': conversation_id})
    
    # Check if the conversation exists
    if conversation:
        print(f"Conversation ID: {conversation_id}")
        print(f"Model Used: {conversation['model_used']}")  
        print("=" * 50)
        
        for i, interaction in enumerate(conversation['interactions'], 1):
            print(f"Interaction #{i}")
            print(f"User: {interaction['query']}")
            print(f"Chatbot: {interaction['response']}")
            print(f"Timestamp: {interaction['timestamp']}")
            print("-" * 50)
            
    else:
        print(f"No conversation found with ID: {conversation_id}")

    