Connect to Intelligent Mongodb

Local Development
0. Install pymongo and datetime: "pip install pymongo".

1. Open git ignore and add ".streamlit" and "secrets.toml".

2. Create a new directory in the project root directory called ".streamlit".

3. Inside of ".streamlit" create a file called secrets.toml.

4. place the connection string with your password in the secrets.toml file (SERVER_URL = "mongodb+srv://<username>:<password>@intelligentui.9to7zvv.mongodb.net/?retryWrites=true&w=majority").

4.5 Note: you should also use this document to save your OpenAI api key as OPENAI_API_KEY = <your key> and call it with api_key = st.secrets["OPENAI_API_KEY"]. Doing so will ensure that your code will continue to work with the deployed app on streamlit community cloud.

5. Change the value for the collection_name variable in the mongodb_conversation_logging module to "conversations_david". This will ensure that different query-response formats are not stored in the same collection. 

5. Import from mongodb_converastion_logging import connect_mongodb_collection, initialize_conversation, update_conversation in main.py.

6. To ensure the entire conversation with the user is captured in the same document, initialize a new session state to hold the conversation id: session.state.conversation_id = initialize_conversation(model_name = model_name), then pass conversation_id = session.state.conversation_id to the update_conversation(). This is better for user expereince tracking. 

7. Alternativly store each query-response pair in its own document by resetting the the conversation_id each run through streamlit by assigning it to a python variable: conversation_id = initialize_conversation(model_name = model_name). This is likely going to be easier to use for training a model. 