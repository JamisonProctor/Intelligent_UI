from typing import List, Optional
from pydantic import BaseModel, Field

class UI_INSTRUCTIONS_FORMAT(BaseModel):

    # Detailed definitions for each UI element.
    # For simplicity, only the first three elements are shown. Extend as needed.

    """   
    ui_element_1_label: str = Field(description="Refernce the content of the query. Offer a leading topic which will allow the reader to dive deeper into a specific aspect of the information.")
    ui_element_1_options: Optional[List[str]] = Field(description="A list of options related to the label, which the reader will select to show what information they want to explore.")
    ui_element_1_type: str = Field(description='Considering the options from above choose which UI element would be best from this list: "TextInput", "Button", "ListofButtons", "Checkbox", "MultiSelect", "Slider", "SelectSlider". "Slider" or "SelectSlider" should only be used for numerical content. If the information is categorical, then "Checkbox" should be used.')
    ui_element_1_min_value: Optional[int] = Field(description="The minimum value for the first UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_1_max_value: Optional[int] = Field(description="The maximum value for the first UI element, if applicable Carefully consider the range of values that are appropriate for the topic.")

    ui_element_2_label: str = Field(description="Refernce the content of the query. Offer a leading topic which will allow the reader to dive deeper into a specific aspect of the information.")
    ui_element_2_options: Optional[List[str]] = Field(description="A list of options related to the label, which the reader will select to show what information they want to explore.")
    ui_element_2_type: str = Field(description='Considering the options from above choose which UI element would be best from this list: "TextInput", "Button", "ListofButtons", "Checkbox", "MultiSelect", "Slider", "SelectSlider". "Slider" or "SelectSlider" should only be used for numerical content. If the information is categorical, then "Checkbox" should be used.')
    ui_element_2_min_value: Optional[int] = Field(description="The minimum value for the first UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_2_max_value: Optional[int] = Field(description="The maximum value for the first UI element, if applicable Carefully consider the range of values that are appropriate for the topic.")


    ui_element_3_label: str = Field(description="Refernce the content of the query. Offer a leading topic which will allow the reader to dive deeper into a specific aspect of the information, if applicable.")
    ui_element_3_options: Optional[List[str]] = Field(description="A list of options related to the label, which the reader will select to show what information they want to explore.")
    ui_element_3_type: str = Field(description='Considering the options from above choose which UI element would be best from this list: "TextInput", "Button", "ListofButtons", "Checkbox", "MultiSelect", "Slider", "SelectSlider". "Slider" or "SelectSlider" should only be used for numerical content. If the information is categorical, then "Checkbox" should be used. Often a text input allowing the user to input whatever question they might have is the best choice here.')
    ui_element_3_min_value: Optional[int] = Field(description="The minimum value for the first UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_3_max_value: Optional[int] = Field(description="The maximum value for the first UI element, if applicable Carefully consider the range of values that are appropriate for the topic.")
    """
    ui_element_1_type: str = Field(description='Choose the most relevant UI element for the first element from this list: "TextInput", "Button", "ListofButtons", "Checkbox", "MultiSelect", "Slider", "SelectSlider". "Slider" or "SelectSlider" should only be used if the content is numerical and the numbers should be relvant to the topic. Think carefully! If the information is categorical, then "ListofButtons" or "Checkbox" should be used.')
    ui_element_1_label: str = Field(description="A topically relevent label for the first UI element")
    ui_element_1_options: Optional[List[str]] = Field(description="A list of options considering the overview content for the first UI element, if applicable")
    ui_element_1_min_value: Optional[int] = Field(description="The minimum value for the first UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_1_max_value: Optional[int] = Field(description="The maximum value for the first UI element, if applicable Carefully consider the range of values that are appropriate for the topic.")

    ui_element_2_type: Optional[str] = Field(description='Choose the next most relevant UI element for the second element from this list: "TextInput", "Button", "ListofButtons", "Checkbox", "MultiSelect", "Slider", "SelectSlider", if applicable. "Slider" or "SelectSlider" should only be used if the content is numerical and the numbers should be relvant to the topic. Think carefully! If the information is categorical, then "ListofButtons"  or "Checkbox" should be used.')
    ui_element_2_label: Optional[str] = Field(description="A topically relevent label for the second UI element")
    ui_element_2_options: Optional[List[str]] = Field(description="A list of options considering the overview content for the second UI element, if applicable")
    ui_element_2_min_value: Optional[int] = Field(description="The minimum value for the second UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_2_max_value: Optional[int] = Field(description="The maximum value for the second UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")

    ui_element_3_type: Optional[str] = Field(description='Choose the next most relevant UI element for the third element from this list: "TextInput", "Button", "ListofButtons",  "Checkbox", "MultiSelect", "Slider", "SelectSlider", if applicable. "Slider" or "SelectSlider" should only be used if the content is numerical and the numbers should be relvant to the topic. Think carefully! If the information is categorical, then "ListofButtons" or "Checkbox" should be used. Often a text input allowing the user to input whatever question they might have is the best choice here.')
    ui_element_3_label: Optional[str] = Field(description="A topically relevent label for the third UI element")
    ui_element_3_options: Optional[List[str]] = Field(description="A list of options considering the overview content for the third UI element, if applicable")
    ui_element_3_min_value: Optional[int] = Field(description="The minimum value for the third UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")
    ui_element_3_max_value: Optional[int] = Field(description="The maximum value for the third UI element, if applicable. Carefully consider the range of values that are appropriate for the topic.")

class CONTENT_INSTRUCTIONS_FORMAT(BaseModel):

    Overview: str = Field(description="Provide a detailed, educational response that keeps the reader engaged. Add humor and emojis for a fun touch. 🎉🤓")
    #Overview_label: str = Field(description="A topically relevent label. Can be funny")
    Title: str = Field(description="The title of the topic. Alway add contextual emojis!!.")
