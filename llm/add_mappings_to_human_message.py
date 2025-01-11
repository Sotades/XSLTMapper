"""Module for adding mappings to human messages from Excel files."""

from typing import List, Dict, Any
from pathlib import Path
from excelutils.excel_reader import ExcelReader
from langchain.schema import HumanMessage


def add_mappings_to_human_message(excel_sheet: str, human_message: HumanMessage) ->  HumanMessage:
    """Read mappings from Excel file.
    
    Args:
        excel_sheet: Path to Excel file containing mappings
        
    Returns:
        List of dictionaries containing mapping data
        
    Raises:
        FileNotFoundError: If Excel file doesn't exist
        ValueError: If Excel file format is invalid
    """
    # Validate file exists
    file_path = Path(excel_sheet)
    if not file_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_sheet}")
    
    # Read mappings from Excel
    reader = ExcelReader(file_path)
    try:
        mappings = reader.read_worksheet(
            worksheet_name="Mappings",
            header=True,
            start_row=1
        )
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")
    finally:
        reader.close()

    # Validate required columns exist
    required_columns = ['Input XPath', 'Output XPath', 'Special Instructions']
    missing_columns = [col for col in required_columns if col not in mappings[0]]
    if missing_columns:
        raise ValueError(f"Excel file missing required columns: {', '.join(missing_columns)}")
    
    # Create a HumanMessage object
    human_message = HumanMessage(content="")
    
    # Set template variables for each row
    for mapping in mappings:
        mapping['input_xpath'] = mapping.pop('Input XPath')
        mapping['output_xpath'] = mapping.pop('Output XPath') 
        mapping['special_instructions'] = mapping.pop('Special Instructions')

        mapping_text = f"""\n-Input XPath: {mapping['input_xpath']}\nOutput XPath: {mapping['output_xpath']}\nSpecial Instructions:\n{mapping['special_instructions']}\n"""
        # Append mapping_text to human message
        human_message.content += mapping_text


    return human_message

