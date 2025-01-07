"""Test module for LLM operations."""

from llmtemp.llm import do_llm


def test_simple_llm_call():
    """Test a simple call to do_llm."""
    response = do_llm(
        prompt="What is Python?",
        model="gpt-4",
        temperature=1
    )
    print(f"LLM Response: {response}")


if __name__ == "__main__":
    test_simple_llm_call()
