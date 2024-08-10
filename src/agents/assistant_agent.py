# Define the assistant agent
# assistant_agent.py
from .base_agent import BaseAgent
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent

class AssistantAgent(BaseAgent, RetrieveAssistantAgent):
    def __init__(self, name, system_message, llm_config):
        BaseAgent.__init__(self, name)
        RetrieveAssistantAgent.__init__(self, name=name, system_message=system_message, llm_config=llm_config)
