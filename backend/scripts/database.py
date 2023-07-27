import os
from dotenv import load_dotenv
import pymongo

dotenv_path = os.getdotenv_path = os.path.join(os.getcwd(), "backend/.env")
_ = load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")

client = pymongo.MongoClient(MONGODB_URI)

dblist = client.list_database_names()

slr_db = None
slr_collection = None


def initialise_db():
    global slr_db
    global slr_collection

    data_stucture = {
        "_id": "string",
        "messages": {"question": "string", "response": "string"},
    }

    if "slr" in dblist:
        slr_db = client["slr"]
        slr_collection = slr_db["chat_history"]
    else:
        slr_db = client["slr"]
        slr_collection = slr_db["chat_history"]
        slr_collection.insert_one(data_stucture)
        print("Created an slr database with chat_history collection")


def get_chat_history(id):
    initialise_db()
    chat = slr_collection.find_one({"_id": id})
    messages = chat["messages"]
    print(messages)


get_chat_history("string")
