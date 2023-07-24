import os
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
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
loader = UnstructuredPDFLoader("documents/pdfs/photography.pdf")
# pages = loader.load_and_split()
pages = loader.load()

# split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=350,
    chunk_overlap=25,
)
docs = text_splitter.split_documents(pages)

# create vector store folder
folder = Path(output_directory)
if folder.exists():
    for file in folder.glob("*"):
        file.unlink()  # remove all files and subdirectories
else:
    folder.mkdir(parents=True, exist_ok=True)  # create folder

# create vector store
vectordb = FAISS.from_documents(
    docs,
    embeddings,
)

# save vector store
vectordb.save_local(output_directory)

print(f"{len(docs)} docs saved to vector store")
