import os
from typing import Literal
from tavily import TavilyClient
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from deepagents import create_deep_agent
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from tools import internet_search, document_findings, send_email

load_dotenv() 



# Initialize Langfuse client
langfuse = get_client()
 
# Verify connection
if langfuse.auth_check():
    print("Langfuse client is authenticated and ready!")
else:
    print("Authentication failed. Please check your credentials and host.")
 
# Initialize Langfuse CallbackHandler for LangChain (tracing)
langfuse_handler = CallbackHandler()


# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to subagents that can help you with data collection, documentation, and sharing of findings.
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

# Create subagents
data_collector_subagent = {
    "name": "data-collector-agent",
    "description": "Searches internet and available database for data",
    "system_prompt": "You are a data collection specialist. Your role is to search the internet and databases to gather relevant information and data for research purposes.",
    "tools": [internet_search],
    "model": "azure_openai:gpt-4.1",  # Optional override, defaults to main agent model
}

documentation_subagent = {
    "name": "documentation-sharing-agent",
    "description": "Documents findings and shares them via email",
    "system_prompt": "You are a documentation and sharing specialist. Your role is to document research findings in markdown format and share summaries via email.",
    "tools": [document_findings, send_email],
    "model": "azure_openai:gpt-4.1",  # Optional override, defaults to main agent model
}

subagents = [data_collector_subagent, documentation_subagent]

agent = create_deep_agent(
    model=model,
    subagents=subagents,
    system_prompt=research_instructions
)


# Invoke the agent with Langfuse tracing
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Search from internet about latest gpt model in 2025 and provide summary about it and share it via email to spiderman@gmail.com"}]}, 
    config={"callbacks": [langfuse_handler]}
)

# Print the agent's response
print(result["messages"][-1].content)

print("END")