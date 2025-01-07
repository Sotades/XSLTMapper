"""Module for handling LLM operations using Langchain."""

from pathlib import Path
from typing import Optional, Dict, Any
from langchain.prompts import SystemMessagePromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()


def do_llm(
    prompt: str,
    system_prompt_file: str = "llmtemp/system_prompt.txt",
    model: str = "gpt-4o",
    temperature: float = 1,
    **kwargs: Dict[str, Any]
) -> str:
    """Execute LLM call using Langchain with system prompt from file.
    
    Args:
        prompt: The user prompt to send to the LLM
        system_prompt_file: Path to system prompt template file (default: system_prompt.txt)
        model: The model to use (default: gpt-3.5-turbo)
        temperature: Sampling temperature (default: 0.7)
        **kwargs: Additional keyword arguments for formatting system prompt
    
    Returns:
        str: The LLM response
        
    Raises:
        FileNotFoundError: If system prompt file doesn't exist
        ValueError: If prompt is empty
    """
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty")

    # Read and create system message template
    system_prompt_path = Path(system_prompt_file)
    if not system_prompt_path.exists():
        raise FileNotFoundError(f"System prompt file not found: {system_prompt_file}")
    
    with open(system_prompt_path, 'r', encoding='utf-8') as file:
        template = file.read()
    
    system_message_template = SystemMessagePromptTemplate.from_template(template)
    system_message = system_message_template.format(**kwargs)
    
    # Initialize chat model
    chat = ChatOpenAI(
        model_name=model,
        temperature=temperature
    )
    
    # Create messages and execute LLM call
    messages = [
        system_message,
        HumanMessage(content=prompt)
    ]
    
    try:
        response = chat(messages)
        return response.content
    except Exception as e:
        raise RuntimeError(f"Error during LLM call: {str(e)}") from e
