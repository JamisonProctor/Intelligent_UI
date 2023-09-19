import streamlit as st
#from json_handler import ui_instructions

ui_instructions = {'Overview': 'Dinosaurs are a group of reptiles that appeared during the Mesozoic Era, between 230 and 65 million years ago. They are known for their size, with some reaching up to 100 feet long and others as small as a chicken. Dinosaurs are a diverse group, with various shapes, sizes, and dietary preferences. 🦖🦕',
 'Overview_label': 'Dino 101',
 'Title': 'Dinosaurs 🦖🦕',
 'ui_element_1_type': 'SelectSlider',
 'ui_element_1_label': 'Choose a period',
 'ui_element_1_options': ['Triassic', 'Jurassic', 'Cretaceous'],
 'ui_element_1_min_value': None,
 'ui_element_1_max_value': None,
 'ui_element_2_type': 'Checkbox',
 'ui_element_2_label': 'Diet Preference',
 'ui_element_2_options': ['Herbivore', 'Carnivore', 'Omnivore'],
 'ui_element_2_min_value': None,
 'ui_element_2_max_value': None,
 'ui_element_3_type': 'TextInput',
 'ui_element_3_label': "Any specific dinosaur you're interested in?",
 'ui_element_3_options': None,
 'ui_element_3_min_value': None,
 'ui_element_3_max_value': None}

#def ui_generator(ui_instructions):

st.title(ui_instructions["Title"])
st.markdown(f'**{ui_instructions["Overview_label"]}**')
st.write(ui_instructions["Overview"])

# Initialize session state for user_inputs if it doesn't exist
if 'user_inputs' not in st.session_state:
    st.session_state.user_inputs = {}

for i in range(1, 5):  # Adjust as needed.
    element_type = ui_instructions.get(f'ui_element_{i}_type')
    label = ui_instructions.get(f'ui_element_{i}_label')
    options = ui_instructions.get(f'ui_element_{i}_options')
    min_value = ui_instructions.get(f'ui_element_{i}_min_value')
    max_value = ui_instructions.get(f'ui_element_{i}_max_value')

    if element_type == "Checkbox":
        # Checkbox does not support a native label. So, we'll add it manually.
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
        if min_value is None or max_value is None:  # This means it should be a selectbox instead
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
        # This element type doesn't have a built-in label, so we'll add it
        st.write(f"{label}")
        if label not in st.session_state.user_inputs:
            st.session_state.user_inputs[label] = []
        
        for opt in options:
            if st.button(opt, key=f'button_{opt}'):
                if opt not in st.session_state.user_inputs[label]:
                    st.session_state.user_inputs[label].append(opt)
                    
# Add the confirm button at the end
if st.button("Confirm"):
    confirmed_inputs = st.session_state.user_inputs.copy()
    st.write("Confirmed Inputs:")
    st.write(confirmed_inputs)