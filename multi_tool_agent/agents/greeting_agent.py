from typing import Optional

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent.constants import MODEL_GEMINI_2_0_FLASH

def say_hello(name: Optional[str] = None):
    """Provides a simple greeting, optionally addressing the user by name.

    Args:
        name (str, optional): The name of the person to greet. Don't pass anything if you don't know users name

    Returns:
        str: A friendly greeting message.
    """
    if name is None:
        name = "there"
    return f"Hello, {name}!"

def create_greeting_agent(model, model_type):
    try:
        model_to_use = model
        if model != MODEL_GEMINI_2_0_FLASH:  # gemini is not supported by light llm (vertex ai creds will be required)
            model_to_use = LiteLlm(model=model)
        return Agent(
            name="greeting_agent_v1_" + model_type,
            model=model_to_use,
            instruction="You are the Greeting Agent. Your ONLY task is to provide a friendly greeting to the user. "
                        "Use the 'say_hello' tool to generate the greeting. "
                        "If the user provides their name, make sure to pass it to the tool. "
                        "Do not engage in any other conversation or tasks.",
            tools=[say_hello],
        )
    except Exception as e:
        print(f"An error occurred while creating greeting agent, {e}")
        raise
