from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent.constants import MODEL_GEMINI_2_0_FLASH


def say_goodbye() -> str:
    """Provides a simple farewell message to conclude the conversation."""
    return "Goodbye! Have a great day."


def create_farewell_agent(model, model_type):
    try:
        model_to_use = model
        if model != MODEL_GEMINI_2_0_FLASH:  # gemini is not supported by light llm (vertex ai creds will be required)
            model_to_use = LiteLlm(model=model)
        return Agent(
            name="farewell_agent_v1_" + model_type,
            model=model_to_use,
            instruction="You are the Farewell Agent. Your ONLY task is to provide a polite goodbye message. "
                        "Use the 'say_goodbye' tool when the user indicates they are leaving or ending the conversation "
                        "(e.g., using words like 'bye', 'goodbye', 'thanks bye', 'see you'). "
                        "Do not perform any other actions.",
            tools=[say_goodbye],
        )
    except Exception as e:
        print(f"An error occurred while creating farewell agent, {e}")
        raise
