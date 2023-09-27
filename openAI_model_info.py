import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
import streamlit as st

#load_dotenv()
#api_key = os.getenv('OPENAI_API_KEY')

api_key = st.secrets["OPENAI_API_KEY"]

#choose model
#model_name = 'gpt-3.5-turbo'
#model_name = 'gpt-3.5-turbo-16k'
model_name = 'gpt-4'
#model_name = 'text-davinci-003' #not working
temperature = 0.2


