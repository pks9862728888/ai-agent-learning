# --- Session Management ---
# Key Concept: SessionService stores conversation history & state.
# InMemorySessionService is simple, non-persistent storage for this tutorial.
from google.adk import Runner
from google.adk.sessions import InMemorySessionService

from multi_tool_agent.constants import APP_NAME, USER_ID, SESSION_ID
from multi_tool_agent.weather_agent import weather_agent

session_service = InMemorySessionService()

# Create the specific session where the conversation will happen
session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

runner = Runner(
    agent=weather_agent, # The agent we want to run
    app_name=APP_NAME,   # Associates runs with our app
    session_service=session_service # Uses our session manager
)
