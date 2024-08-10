# Functions to handle embeddings
# embedding_utils.py
from chromadb.utils import embedding_functions

def get_openai_embedding_function(api_key):
    return embedding_functions.OpenAIEmbeddingFunction(api_key=api_key)
