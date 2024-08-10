# Entry point to initiate the agents
# main.py
import autogen_utils
from agents.assistant_agent import AssistantAgent
from agents.user_proxy_agent import UserProxyAgent

def main():
    config = autogen_utils.load_config()
    assistant = AssistantAgent("assistant", "You are a helpful assistant.", config)
    rag_agent = UserProxyAgent(config, "NEVER")
    
    assistant.reset()
    rag_agent.initiate_chat(assistant, problem="What is the workflow in docGPT?", n_results=2)

if __name__ == "__main__":
    main()
