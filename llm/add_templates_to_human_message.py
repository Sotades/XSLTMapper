"""Module for adding templates to human messages from Excel files."""

from typing import List, Dict, Any
from pathlib import Path
from excelutils.excel_reader import ExcelReader
from langchain.schema import HumanMessage


def add_templates_to_human_message(excel_sheet: str) ->  HumanMessage:
    """Read templates from Excel file.
    
    Args:
        excel_sheet: Path to Excel file containing templates
        
    Returns:
        List of dictionaries containing template data
        
    Raises:
        FileNotFoundError: If Excel file doesn't exist
        ValueError: If Excel file format is invalid
    """
    # Validate file exists
    file_path = Path(excel_sheet)
    if not file_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_sheet}")
    
    # Read templates from Excel
    reader = ExcelReader(file_path)
    try:
        templates = reader.read_worksheet(
            worksheet_name="Templates",
            header=True,
            start_row=1
        )
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")
    finally:
        reader.close()

    # Validate required columns exist
    required_columns = ['Template Mode', 'Template Match', 'Template Instructions']
    missing_columns = [col for col in required_columns if col not in templates[0]]
    if missing_columns:
        raise ValueError(f"Excel file missing required columns: {', '.join(missing_columns)}")
    
    # Create a HumanMessage object
    human_message = HumanMessage(content="")
    
    # Set template variables for each row
    for template in templates:
        template['template_mode'] = template.pop('Template Mode')
        template['template_match'] = template.pop('Template Match') 
        template['template_instructions'] = template.pop('Template Instructions')

        template_text = f"""- Template:\nTemplate Mode: {template['template_mode']}\nTemplate Match: {template['template_match']}\nTemplate Instructions:\n{template['template_instructions']}\n"""
        # Append template_text to human message
        human_message.content += template_text


    return human_message

