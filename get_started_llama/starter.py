# import logging
# import sys

from llama_index import VectorStoreIndex, SimpleDirectoryReader

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
# index.storage_context.persist()


query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)