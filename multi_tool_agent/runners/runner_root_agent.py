# --- Session Management ---
# Key Concept: SessionService stores conversation history & state.
# InMemorySessionService is simple, non-persistent storage for this tutorial.
from google.adk import Runner
from google.adk.sessions import InMemorySessionService

from multi_tool_agent.agents.root_agent import root_agent_gemini
from multi_tool_agent.constants import APP_NAME, USER_ID, SESSION_ID, GEMINI

root_agent_user_session_service = InMemorySessionService()

# Create the specific session where the conversation will happen
session = root_agent_user_session_service.create_session(
    app_name=APP_NAME + GEMINI,
    user_id=USER_ID + GEMINI,
    session_id=SESSION_ID + GEMINI
)

root_agent_runner_gemini = Runner(
    agent=root_agent_gemini,  # The agent we want to run
    app_name=APP_NAME + GEMINI,  # Associates runs with our app
    session_service=root_agent_user_session_service  # Uses our session manager
)
