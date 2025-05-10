# --- Session Management ---
# Key Concept: SessionService stores conversation history & state.
# InMemorySessionService is simple, non-persistent storage for this tutorial.
from google.adk import Runner
from google.adk.sessions import InMemorySessionService

from multi_tool_agent.constants import APP_NAME, USER_ID, SESSION_ID
from multi_tool_agent.weather_agent import weather_agent_anthropic

weather_agent_user_session_service = InMemorySessionService()

ANTHROPIC = "anthropic"

# Create the specific session where the conversation will happen
session = weather_agent_user_session_service.create_session(
    app_name=APP_NAME + ANTHROPIC,
    user_id=USER_ID + ANTHROPIC,
    session_id=SESSION_ID + ANTHROPIC
)

weather_agent_runner_anthropic = Runner(
    agent=weather_agent_anthropic,  # The agent we want to run
    app_name=APP_NAME + ANTHROPIC,  # Associates runs with our app
    session_service=weather_agent_user_session_service  # Uses our session manager
)
