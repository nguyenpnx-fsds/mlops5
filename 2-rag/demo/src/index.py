from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
import pandas as pd

from settings import SETTINGS


# Load the dataset
df = pd.read_parquet(
    "hf://datasets/rag-datasets/rag-mini-wikipedia/data/passages.parquet/part.0.parquet"
)

# Create a list of Document objects
docs = [Document(page_content=passage) for passage in df.passage.values]


# Split the documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)


# Create an in-memory vector store and add the documents
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=SETTINGS.OPENAI_API_KEY,
)
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(documents=all_splits)
