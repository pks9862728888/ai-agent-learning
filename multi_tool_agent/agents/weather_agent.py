from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from multi_tool_agent.constants import *


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city (e.g., "New York", "London", "Tokyo").

    Returns:
        dict: A dictionary containing the weather information.
              Includes a 'status' key ('success' or 'error').
              If 'success', includes a 'report' key with weather details.
              If 'error', includes an 'error_message' key.
    """
    normalized_city = city.lower().replace(" ", "")  # basic normalization of input

    # Mock weather data
    mock_weather_db = {
        "newyork": {"status": "success", "report": "The weather in New York is sunny with a temperature of 25°C."},
        "london": {"status": "success", "report": "It's cloudy in London with a temperature of 15°C."},
        "tokyo": {"status": "success", "report": "Tokyo is experiencing light rain and a temperature of 18°C."},
    }

    if normalized_city in mock_weather_db:
        return mock_weather_db[normalized_city]
    else:
        return {"status": "error", "error_message": f"Weather information for '{city}' is not available."}


def create_weather_agent(model, model_type):
    try:
        model_to_use = model
        if model != MODEL_GEMINI_2_0_FLASH:  # gemini is not supported by light llm (vertex ai creds will be required)
            model_to_use = LiteLlm(model=model)
        return Agent(
            name="weather_agent_v1_" + model_type,
            model=model_to_use,
            description=(
                "Provides weather information for specific cities."
            ),
            instruction="You are a helpful weather assistant. "
                        "When the user asks for the weather in a specific city, "
                        "use the 'get_weather' tool to find the information. "
                        "If the tool returns an error, inform the user politely. "
                        "If the tool is successful, present the weather report clearly.",
            tools=[get_weather]
        )
    except Exception as e:
        print(f"An error occurred while creating weather agent, {e}")
        raise
