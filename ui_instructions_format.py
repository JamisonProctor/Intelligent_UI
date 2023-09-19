"""
ui_instructions_format.py

This module defines the UI_INSTRUCTIONS_FORMAT class, which provides a structured format
for UI instructions, complete with validation and documentation for each field.
"""

from typing import List, Optional
from pydantic import BaseModel, Field

class UI_INSTRUCTIONS_FORMAT(BaseModel):
    """
    A Pydantic model that represents the format for UI instructions.

    Attributes:
    - Overview: A brief description of the topic, aiming to pique the user's interest.
    - Overview_label: A label associated with the overview.
    - Title: The main title of the topic.
    - ui_element_{i}_type: Specifies the UI element type for the i-th element.
    - ui_element_{i}_label: A label associated with the i-th UI element.
    - ui_element_{i}_options: A list of options for the i-th UI element.
    - ui_element_{i}_min_value: Minimum value (if applicable) for the i-th UI element.
    - ui_element_{i}_max_value: Maximum value (if applicable) for the i-th UI element.
    
    Note: The class can support multiple UI elements with a sequential naming pattern.
    """ 

    Overview: str = Field(description="Deep dive into the core essence of the query, unveiling rich layers of information and detail. Paint a vivid, educational, and insightful picture about the topic, ensuring the reader hungers for more. 🤓 While presenting data, sprinkle in humor where apt and enhance the narrative with emojis for that delightful touch. 🎉 Let's make learning fun and engaging! 🚀")
    Overview_label: str = Field(description="A topically relevent label. Can be funny")
    Title: str = Field(description="The title of the topic. Alway add contextual emojis!!.")

    # Detailed definitions for each UI element.
    # For simplicity, only the first three elements are shown. Extend as needed.

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
