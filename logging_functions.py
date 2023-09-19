import uuid
import sqlite3

db_path = 'conversations.db'

def setup_database():
    """
    Set up the SQLite database and create a table for conversations if it doesn't exist.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY,
        conversation_id TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        content TEXT NOT NULL,
        type TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def get_next_conversation_id():
    """
    Fetch the current maximum conversation ID and return the next ID.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT MAX(id) FROM conversations')
    row = cursor.fetchone()
    
    if row[0] is None:
        conversation_id = 1
    else:
        conversation_id = row[0] + 1

    conn.close()

    return conversation_id


def start_new_conversation():
    # Generate a new unique conversation_id
    return str(uuid.uuid4())

def log_content(conversation_id, content, content_type):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Check if content is already in the db for this conversation_id
    cursor.execute('''
    SELECT content FROM conversations WHERE conversation_id=? ORDER BY id DESC LIMIT 1
    ''', (conversation_id,))
    last_content = cursor.fetchone()
    if last_content and last_content[0] == content:
        return  # Don't insert repeated content

    # Insert new content
    cursor.execute('''
    INSERT INTO conversations (conversation_id, content, type) VALUES (?, ?, ?)
    ''', (conversation_id, content, content_type))
    conn.commit()
    conn.close()
