"""Main module for LLM operations."""
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from llm.system_message import create_system_message
from llm.add_templates_to_human_message import add_templates_to_human_message
from llm.add_mappings_to_human_message import add_mappings_to_human_message
from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

def main():
    """Execute main LLM workflow."""
    try:
        # Create system message
        system_message = create_system_message()
        print("\nSystem Message:")
        print("-" * 50)
        print(system_message.content)
        
        # Create human messages
        spreadsheet_path = Path("mapping_spec/Mapping Specification.xlsx")
        human_message = add_templates_to_human_message(spreadsheet_path)
        human_message = add_mappings_to_human_message(spreadsheet_path, human_message)
        
        print("\nHuman Message:")
        print("-" * 50)
        print(human_message.content)

        # Combine the system and user messages into a chat prompt
        chat_prompt = ChatPromptTemplate.from_messages([
            system_message,
            human_message
        ])

        # Create a chat model
        chat_model = ChatOpenAI(model="gpt-4o", max_tokens=8096)

        # Generate a response using the LLM
        messages = chat_prompt.format_messages()
        response = chat_model(messages)
        
        # Output the response
        print(response.content)
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main() 