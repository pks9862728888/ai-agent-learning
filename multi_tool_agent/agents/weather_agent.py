from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import ToolContext

from multi_tool_agent.constants import *


def get_weather(city: str, tool_context: ToolContext) -> dict:
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

    preferred_unit = tool_context.state.get("user_preference_temperature_unit", "Celsius")  # Default to Celsius


    # Mock weather data (always stored in Celsius internally)
    mock_weather_db = {
        "newyork": {"temp_c": 25, "condition": "sunny"},
        "london": {"temp_c": 15, "condition": "cloudy"},
        "tokyo": {"temp_c": 18, "condition": "light rain"},
    }

    if normalized_city in mock_weather_db:
        data = mock_weather_db[normalized_city]
        temp_c = data["temp_c"]
        condition = data["condition"]

        # Format temperature based on state preference
        if preferred_unit == "Fahrenheit":
            temp_value = (temp_c * 9/5) + 32 # Calculate Fahrenheit
            temp_unit = "°F"
        else: # Default to Celsius
            temp_value = temp_c
            temp_unit = "°C"

        report = f"The weather in {city.capitalize()} is {condition} with a temperature of {temp_value:.0f}{temp_unit}."
        result = {"status": "success", "report": report}

        # Example of writing back to state (optional for this tool)
        tool_context.state["last_city_checked_stateful"] = city

        return result
    else:
        # Handle city not found
        error_msg = f"Sorry, I don't have weather information for '{city}'."
        return {"status": "error", "error_message": error_msg}


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
            tools=[get_weather],
            output_key="last_weather_report"
        )
    except Exception as e:
        print(f"An error occurred while creating weather agent, {e}")
        raise
