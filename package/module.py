import os
from typing import Literal
from tavily import TavilyClient
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent

load_dotenv() 
tavily_api_key = os.environ["TAVILY_API_KEY"]


tavily_client = TavilyClient(api_key=tavily_api_key)

def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
):
    """Run a web search"""
    return tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )


# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

llm = AzureChatOpenAI(
    azure_deployment="gpt-4.1",  # or your deployment
    api_version="2024-08-01-preview",  # or your api version
    temperature=0,
)


model = llm

# model = init_chat_model(
#     model=AzureChatOpenAI(
#         azure_deployment="gpt-4.1",  # or your deployment
#         api_version="2024-08-01-preview",  # or your api version
#         temperature=0,
#     )
# )

# model = init_chat_model(model="gpt-4.1", model_provider="azure_openai")

agent = create_deep_agent(
    model=model,
    tools=[internet_search],
    system_prompt=research_instructions
)


result = agent.invoke({"messages": [{"role": "user", "content": "Who is ben 10"}]})

# Print the agent's response
print(result["messages"][-1].content)