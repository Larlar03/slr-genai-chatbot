import os
import shutil
from dotenv import load_dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


# get api key
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
dotenv_path = os.path.join(parent_dir, ".env")
_ = load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# load data
loader = CSVLoader(file_path="../documents/events.csv")
event_data = loader.load()
len(event_data)

# get OpenAi embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# create vector store
vectordb_directory = "../documents/faiss_db"
shutil.rmtree(vectordb_directory)  # remove old database files if any

vectordb = FAISS.from_documents(
    event_data,
    embeddings,
)

# save vector store
vectordb.save_local(vectordb_directory)
