import os
from dotenv import load_dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from pathlib import Path

# get api key
current_dir = os.getcwd()
dotenv_path = os.path.join(current_dir, ".env")
_ = load_dotenv(dotenv_path)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# vector store path
output_directory = "documents/faiss_db"

# get OpenAi embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# load data
loader = CSVLoader(file_path="documents/events.csv")
event_data = loader.load()
len(event_data)

# create vector store
folder = Path(output_directory)
if folder.exists():
    for file in folder.glob("*"):
        file.unlink()  # remove all files and subdirectories
else:
    folder.mkdir(parents=True, exist_ok=True)  # create folder

# create vector store
vectordb = FAISS.from_documents(
    event_data,
    embeddings,
)

# save vector store
vectordb.save_local(output_directory)
