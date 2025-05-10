from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent.agents.farewell_agent import create_farewell_agent
from multi_tool_agent.agents.greeting_agent import create_greeting_agent
from multi_tool_agent.agents.weather_agent import create_weather_agent
from multi_tool_agent.constants import MODEL_GEMINI_2_0_FLASH
from multi_tool_agent.filters.block_keyword_guardrail import block_keyword_guardrail


# @title Define the Root Agent with Sub-Agents
# Ensure sub-agents were created successfully before defining the root agent.

def apologize():
    """Provides a simple greeting, optionally addressing the user by name.

    Args: no args

    Returns:
        str: A friendly apology to indicate that the request can not be served.
    """
    return "Sincere apologies. We are unable to find an appropriate agent to process your query :("


def create_root_agent(model, model_type, weather_agent_gemini, greeting_agent, farewell_agent):
    try:
        model_to_use = model
        if model != MODEL_GEMINI_2_0_FLASH:  # gemini is not supported by light llm (vertex ai creds will be required)
            model_to_use = LiteLlm(model=model)
        return Agent(
            name="root_agent_v1_" + model_type,
            model=model_to_use,
            description="The main coordinator agent. Delegates weather requests or greetings/farewells to specialists.",
            instruction="You are the main coordinator Agent coordinating a team. Your primary responsibility is to delegate the request to specialized agents. "
                        "Use the 'apologize' tool ONLY for specific weather requests when you are not able to delegate to any of sub-agents. "
                        "You have specialized sub-agents: "
                        "1. 'weather_agent_gemini': The primary agent which handles weather related information. Delegate weather related prompts to this. "
                        "2. 'greeting_agent': Handles simple greetings like 'Hi', 'Hello'. Delegate to it for these. "
                        "3. 'farewell_agent': Handles simple farewells like 'Bye', 'See you'. Delegate to it for these. "
                        "Analyze the user's query. If it's a greeting, delegate to 'greeting_agent'. If it's a farewell, delegate to 'farewell_agent'. "
                        "If it's a weather request, delegate to 'weather_agent_gemini'. "
                        "For anything else, respond appropriately or state you cannot handle it using apologize tool call.",
            tools=[apologize],
            sub_agents=[weather_agent_gemini, greeting_agent, farewell_agent],
            before_model_callback=block_keyword_guardrail
        )
    except Exception as e:
        print(f"An error occurred while creating root agent, {e}")
        raise

weather_agent_gemini = create_weather_agent(MODEL_GEMINI_2_0_FLASH, "gemini")
greeting_agent = create_greeting_agent(MODEL_GEMINI_2_0_FLASH, "gemini")
farewell_agent = create_farewell_agent(MODEL_GEMINI_2_0_FLASH, "gemini")
root_agent_gemini = create_root_agent(
    MODEL_GEMINI_2_0_FLASH, "gemini", weather_agent_gemini, greeting_agent, farewell_agent)
