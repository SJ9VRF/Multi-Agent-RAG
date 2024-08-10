# Helper functions for AutoGen setup
# autogen_utils.py
import json

def load_config(path='config/config.json'):
    with open(path, 'r') as config_file:
        config = json.load(config_file)
    return config
