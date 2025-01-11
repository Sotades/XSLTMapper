import pytest
from pathlib import Path
from llm import add_mappings_to_human_message
from llm.add_mappings_to_human_message import add_mappings_to_human_message
from langchain.schema import HumanMessage

def test_add_templates_to_human_message():
    # Test with just the spreadsheet name
    spreadsheet_name = Path("mapping_spec/Mapping Specification.xlsx")

    # Create a HumanMessage object
    human_message = HumanMessage(content="")
    
    # Call function
    human_message = add_mappings_to_human_message(spreadsheet_name, human_message)

    # Assert the result is a HumanMessage object
    assert isinstance(human_message, HumanMessage), "Expected a HumanMessage object"

    # Assert the content of the HumanMessage object is not empty
    assert human_message.content != "", "Expected non-empty content"    
