import asyncio

from multi_tool_agent.aync_agent_caller import call_agent_async
from multi_tool_agent.constants import USER_ID, SESSION_ID
from multi_tool_agent.session import runner

def print_response(value):
    print(f"Agent Response: {value}")

async def run_conversation():
    print_response(await call_agent_async("What is the weather like in London?",
                                          runner=runner,
                                          user_id=USER_ID,
                                          session_id=SESSION_ID))

    print_response(await call_agent_async("How about Paris?",
                                          runner=runner,
                                          user_id=USER_ID,
                                          session_id=SESSION_ID)) # Expecting the tool's error message

    print_response(await call_agent_async("Tell me the weather in New York",
                                          runner=runner,
                                          user_id=USER_ID,
                                          session_id=SESSION_ID))

if __name__ == '__main__':
    try:
        asyncio.run(run_conversation())
    except Exception as e:
        print(f"An error occurred: {e}")
