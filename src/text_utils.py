# Text processing utilities
# text_utils.py
from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter():
    return RecursiveCharacterTextSplitter(separators=["\n\n", "\n", "\r", "\t"])
