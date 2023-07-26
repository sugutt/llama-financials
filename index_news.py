import os, config
from llama_index import VectorStoreIndex, SimpleDirectoryReader

os.environ['OPENAI_APIKEY'] = config.OPENAI_APIKEY
