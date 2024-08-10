# Define the RAG user proxy agent
# user_proxy_agent.py
from .base_agent import BaseAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

class UserProxyAgent(BaseAgent, RetrieveUserProxyAgent):
    def __init__(self, config, human_input_mode):
        BaseAgent.__init__(self, "RAG Agent")
        self.retrieve_config = config
        RetrieveUserProxyAgent.__init__(self, human_input_mode=human_input_mode, retrieve_config=self.retrieve_config)
