import os
from dotenv import load_dotenv
import pymongo

dotenv_path = os.getdotenv_path = os.path.join(os.getcwd(), ".env")
_ = load_dotenv(dotenv_path)

# MONGODB_URI = os.environ.get("MONGODB_URI")
# client = pymongo.MongoClient(MONGODB_URI)

client = pymongo.MongoClient("mongo", 27017)

dblist = client.list_database_names()


def initialise_db():
    try:
        if "slr" in dblist:
            db = client["slr"]
            collection = db["chat_history"]
        else:
            db = client["slr"]
            collection = db["chat_history"]
            collection.insert_one(
                {
                    "_id": "0",
                    "messages": [],
                }
            )
            print("Created database and collection")

        return collection

    except Exception as e:
        print("Error during database initialization:", e)
        return None


def store_chat(id, question, answer):
    try:
        db = client["slr"]
        collection = db["chat_history"]

        new_data = {"question": question, "answer": answer}

        document = collection.find_one({"_id": id})

        if document:
            collection.update_one(
                {"_id": id},
                {"$push": {"messages": new_data}},
            )
            print(f"Updated document: {id}")
        else:
            collection.insert_one({"_id": id, "messages": [new_data]})
            print(f"Created new document: {id}")

    except Exception as e:
        print("Error storing chat", e)


def get_chat_history(id):
    try:
        collection = initialise_db()
        chat = collection.find_one({"_id": id})

        if chat:
            messages = chat.get("messages", [])
        else:
            collection.insert_one(
                {
                    "_id": id,
                    "messages": [],
                }
            )
            chat = collection.find_one({"_id": id})
            messages = chat.get("messages", [])

        print(messages)
        return messages
    except Exception as e:
        print("Error getting chat history", e)
        return None
