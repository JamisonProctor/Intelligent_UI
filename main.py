from ui_instructions_format import UI_INSTRUCTIONS_FORMAT
from openAI_model_info import model_name, temperature, api_key

import json
from pydantic import BaseModel, Field, validator
from typing import List, Optional
import streamlit as st
import time

from langchain.llms import OpenAI
from langchain.chat_models import 
 
 

from langchain.output_parsers import PydanticOutputParser

from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from logging_functions import log_content, setup_database, get_next_conversation_id, start_new_conversation

# Create the table
#setup_database()

# Generate a new unique conversation_id
conversation_id = get_next_conversation_id()

model = OpenAI(model_name=model_name, temperature=temperature, api_key=api_key) 
parser = PydanticOutputParser(pydantic_object=UI_INSTRUCTIONS_FORMAT)


def fetch_ui_instructions(query):
    prompt = PromptTemplate(
        template='''
        You are a a highly knowegeable assitant having a conversation with a curious person.
        Your job is to teach and help the person regarding whatever they ask.
        Think carefully before asnwering them, and ensure that you
        take the entire conversation into account when answering.
                
        In the case that the student has a specific goal, please 
        bring the interation to an end when the time is right. Think
        carefully about this. 
        
        Only respond using the format_instructions.\n
        
        {format_instructions}\n
        {query}\n''',
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    _input = prompt.format_prompt(query=query)
    output = model(_input.to_string())
    return dict(parser.parse(output))


if "initialized" not in st.session_state:
    st.session_state.initialized = False

if st.session_state.get("processing", False):
    st.session_state.processing = False

if not st.session_state.initialized:
    st.title("Intelligent UI 💡")
    st.markdown('''
    Intelligent UI is a user-friendly tool designed to streamline interactions with ChatGPT-4.0 and similar AI text interfaces. With the ability to dynamically generate intuitive UI widgets on the fly, it demystifies AI conversations, making them more accessible to everyone, regardless of their familiarity with prompt engineering or the realm of AI. 
    
    🙏 Please understand that none of this content beyond this page is hardcoded, so please give the program time to process 🙏 
    ''')

    st.markdown('**Choose from one of our demo conversation starters:**')

    demo_prompts = [
        "I want to learn about dinosaurs, but I don't know where to start 🦖",
        "I would like to buy a BMW, but I am not sure which model suits my lifestyle 🚗",
        "I want to vote in the upcoming Bavarian election, but I am not sure who to vote for... 🗳️",
    ]

    for prompt in demo_prompts:
        if st.button(prompt):
            st.session_state.processing = True
            st.write("Processing...")
            time.sleep(1)
            st.session_state.conversation = prompt
            st.session_state.initialized = True
            st.experimental_rerun()

    st.markdown('**Or start a conversation however you like** 🤔 ')
    custom_input = st.text_input("Enter your custom conversation starter")
    if custom_input:
        st.session_state.processing = True
        st.write("Processing...")
        time.sleep(1)
        st.session_state.conversation = custom_input
        st.session_state.initialized = True
        st.experimental_rerun()

else:

    # Only fetch conversation if not present in session state
    if not st.session_state.get("conversation"):
        st.session_state.conversation = conversation_starter
    log_content(conversation_id, st.session_state.conversation, 'conversation')


    # Only fetch ui_instructions if not present in session state or when "Confirm" is clicked
    if not st.session_state.get("ui_instructions"):
        st.session_state.ui_instructions = fetch_ui_instructions(st.session_state.conversation)
    log_content(conversation_id, json.dumps(st.session_state.ui_instructions), 'ui_instructions')
        
    ui_instructions = st.session_state.ui_instructions

    # Display title and overview from the dictionary
    st.title(ui_instructions["Title"])
    st.markdown(f'**{ui_instructions["Overview_label"]}**')
    st.write(ui_instructions["Overview"])

    # Initialize session state for user_inputs if it doesn't exist
    if 'user_inputs' not in st.session_state:
        st.session_state.user_inputs = {}

    # Iterate through the UI elements defined in the dictionary
    for i in range(1, 5):  # Adjust as needed
        element_type = ui_instructions.get(f'ui_element_{i}_type')
        label = ui_instructions.get(f'ui_element_{i}_label')
        options = ui_instructions.get(f'ui_element_{i}_options')
        min_value = ui_instructions.get(f'ui_element_{i}_min_value')
        max_value = ui_instructions.get(f'ui_element_{i}_max_value')

        # Handle each UI element type as specified
        if element_type == "Checkbox":
            st.write(f"{label}")
            if label not in st.session_state.user_inputs:
                st.session_state.user_inputs[label] = []

            for option in options:
                checkbox_value = st.checkbox(option, key=f'checkbox_{option}')
                if checkbox_value:
                    if option not in st.session_state.user_inputs[label]:
                        st.session_state.user_inputs[label].append(option)
                else:
                    if option in st.session_state.user_inputs[label]:
                        st.session_state.user_inputs[label].remove(option)

        elif element_type == "SelectSlider":
            if min_value is None or max_value is None:
                selected_option = st.selectbox(label, options)
                st.session_state.user_inputs[label] = selected_option
            else:
                slider_value = st.slider(label, min_value, max_value)
                st.session_state.user_inputs[label] = slider_value

        elif element_type == "TextInput":
            text_value = st.text_input(label, key=f'text_input_{i}')
            st.session_state.user_inputs[label] = text_value

        elif element_type == "MultiSelect":
            multiselect_value = st.multiselect(label, options, key=f'multiselect_{i}')
            st.session_state.user_inputs[label] = multiselect_value

        elif element_type == "Slider":
            slider_value = st.slider(label, min_value=min_value, max_value=max_value, key=f'slider_{i}')
            st.session_state.user_inputs[label] = slider_value

        elif element_type == "ListofButtons":
            st.write(f"{label}")
            if label not in st.session_state.user_inputs:
                st.session_state.user_inputs[label] = []

            for opt in options:
                if st.button(opt, key=f'button_{opt}'):
                    if opt not in st.session_state.user_inputs[label]:
                        st.session_state.user_inputs[label].append(opt)
    st.write("Once you have selected all the options you want, click confirm to continue. Quit will take you back to the start.")
    col1, col2 = st.columns(2) 

    # Add the confirm button at the end
    if col1.button("Confirm"):
        user_response = st.session_state.user_inputs.copy()
        user_response_string = ", ".join(f"{key}: {value}" for key, value in user_response.items() if value) 
        
        st.session_state.conversation += f'''\n
        Assistant responded: {ui_instructions["Overview"]} \n
        Person responded: Read the following carefully: {user_response_string}. Considering the context provide additional guidance. Make sure there is progress. Think carefully about this. \n
        '''
        
        st.session_state.ui_instructions = fetch_ui_instructions(st.session_state.conversation)
        

        # Clear old user inputs
        st.session_state.user_inputs = {}
        # Refresh the page to start the process over with the new ui_instructions
        st.experimental_rerun()

    if col2.button("Quit"):
        st.session_state.conversation = ""
        st.session_state.user_inputs = {}
        st.session_state.ui_instructions = {}
        st.session_state.initialized = False
        st.experimental_rerun()
