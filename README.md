# About <hr />
ADK is a Python framework designed to streamline the development of applications powered by Large Language Models (LLMs). It offers robust building blocks for creating agents that can reason, plan, utilize tools, interact dynamically with users, and collaborate effectively within a team.

## Instructions followed from <hr />
https://google.github.io/adk-docs/get-started/installation/
https://github.com/google/adk-docs/tree/main/examples/python/tutorial/agent_team/adk-tutorial

# Setup <hr />
python -m venv .venv

.venv\Scripts\activate.bat

pip install google-adk

pip install litellm

## Verify installation <hr />
pip show google-adk

# To move dependencies <hr />
pip freeze > requirements.txt

# To install dependencies <hr />
pip install -r requirements.txt

# API key <hr />
Create an .env file inside multi_tool_agent folder:

Get API key and insert below:

```shell
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=insert api key
```

# Interacting with agent <hr />
- UI based
```adk web```

Open the URL provided (usually http://localhost:8000 or http://127.0.0.1:8000)

- Terminal based:
```shell
adk run multi_tool_agent
```

- Using fast api server
```shell
adk api_server
```
