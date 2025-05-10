import asyncio
import os

from multi_tool_agent.aync_agent_caller import call_agent_async
from multi_tool_agent.constants import USER_ID, SESSION_ID, GEMINI
from multi_tool_agent.runners.runner_root_agent import root_agent_runner_gemini


def print_response(value):
    print(f"Agent Response: {value}")


async def run_conversation(runner, model_type):
    print_response(await call_agent_async("Hello!",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))

    print_response(await call_agent_async("What is the weather like in London?",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))

    print_response(await call_agent_async("How about Paris?",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))  # Expecting the tool's error message

    print_response(await call_agent_async("Tell me the weather in New York",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))

    print_response(await call_agent_async("What event is going on in Hyderabad now?",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))

    print_response(await call_agent_async("Thanks, bye!",
                                          runner=runner,
                                          user_id=USER_ID + model_type,
                                          session_id=SESSION_ID + model_type))


if __name__ == '__main__':
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"
    try:
        asyncio.run(run_conversation(root_agent_runner_gemini, GEMINI))
        # asyncio.run(run_conversation(weather_agent_runner_gemini, GEMINI))
        # asyncio.run(run_conversation(weather_agent_runner_gpt4, GPT))
        # asyncio.run(run_conversation(weather_agent_runner_anthropic, ANTHROPIC))
    except Exception as e:
        print(f"An error occurred: {e}")
