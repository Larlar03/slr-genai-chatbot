import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import MongoDBChatMessageHistory

dotenv_path = os.getdotenv_path = os.path.join(os.getcwd(), "backend/.env")
_ = load_dotenv(dotenv_path)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MONGODB_URI = os.environ.get("MONGODB_URI")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo", temperature=0.5, openai_api_key=OPENAI_API_KEY
)

prompt_template = """You are a chatbot talking to a human who is a photographer. Your goal is to provide human-like responses to their question.
Here are some guidelines to achieve that:
1. Try to understand the context of the conversation and respond accordingly.
2. Use casual language where you can
3. Respond appropriately to greetings, gratitude, and casual language.
4. Use humor and empathy when appropriate.
Don't mention "based on the provded context" or "based on the evidence"
If you don't know the answer, just say that you don't know, don't try to make up an answer.
{chat_history}
Question: {question}
Answer:"""

PROMPT = PromptTemplate.from_template(prompt_template)


def load_vector_store():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = os.path.join(os.getcwd(), "backend/documents/faiss_db")
    vector_store = FAISS.load_local(db, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    return retriever


def get_qa_chain():
    retriever = load_vector_store()
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm, retriever=retriever, memory=memory
    )

    return qa_chain


def store_chat(history, question, response):
    history.add_user_message(question)
    history.add_ai_message(response["answer"])


def get_chat_history(history):
    return history.messages


def prompt_openai(chatId, message):
    message_history = MongoDBChatMessageHistory(
        connection_string=MONGODB_URI, session_id=chatId
    )

    qa_chain = get_qa_chain()
    messages = get_chat_history(message_history)

    question = message

    response = qa_chain({"question": question, "chat_history": messages})

    store_chat(message_history, question=question, response=response)
    print(response["answer"])
    print(messages)


prompt_openai("1", "What shutter speed should I use for sports shots?")
