"""Test module for system message creation."""

from llmtemp.system_message import create_system_message


def test_system_message():
    """Test creating a system message from template."""
    try:
        # Create system message with default template
        system_message = create_system_message()
        print("\nSystem Message Content:")
        print("-" * 50)
        print(system_message.content)
        print("-" * 50)
        
        # Create system message with variables (if your template uses them)
        system_message_with_vars = create_system_message(
            role="Python expert",
            domain="web development"
        )
        print("\nSystem Message with Variables:")
        print("-" * 50)
        print(system_message_with_vars.content)
        print("-" * 50)
        
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    test_system_message() 