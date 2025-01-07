"""Module for creating system messages from template files."""

from pathlib import Path
from typing import Dict, Any, Optional
from langchain.schema import SystemMessage
from langchain.prompts import SystemMessagePromptTemplate


def create_system_message(
    template_file: str = "llmtemp/system_prompt.txt",
    **kwargs: Dict[str, Any]
) -> SystemMessage:
    """Create a system message from a template file.
    
    Args:
        template_file: Path to the system prompt template file
        **kwargs: Variables to format the template with
        
    Returns:
        SystemMessage object
        
    Raises:
        FileNotFoundError: If template file doesn't exist
    """
    # Validate template file exists
    template_path = Path(template_file)
    if not template_path.exists():
        raise FileNotFoundError(f"System prompt template file not found: {template_file}")
    
    # Read template content
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    # Create and format system message
    system_template = SystemMessagePromptTemplate.from_template(template_content)
    system_message = system_template.format(**kwargs)
    
    return system_message 