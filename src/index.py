import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import MongoDBChatMessageHistory

# get api key
current_dir = os.getcwd()
dotenv_path = os.path.join(current_dir, ".env")
_ = load_dotenv(dotenv_path)
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MONGODB_URI = os.environ.get("MONGODB_URI")

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

message_history = MongoDBChatMessageHistory(
    connection_string=MONGODB_URI, session_id="test-session"
)

prompt_template = """You are a help assistant at www.artrabbit.com having a conversation with a person who is looking for something creative adn cultural to do.
Use the following pieces of context to provide a concise answer to the question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Chat History: {chat_history}
Question: {question}
Answer:"""

PROMPT = PromptTemplate.from_template(prompt_template)


def load_vector_store():
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = os.path.join(os.getcwd(), "documents/faiss_db")

    # load vector store
    vector_store = FAISS.load_local(db, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    return retriever


def get_qa_chain():
    retriever = load_vector_store()
    # run question answer chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm, retriever=retriever, memory=memory
    )

    return qa_chain


def store_chat(question, response):
    message_history.add_user_message(question)
    message_history.add_ai_message(response["answer"])


def get_chat_history():
    print(message_history.messages)


def get_chat_messages():
    ...


def prompt_openai():
    qa_chain = get_qa_chain()
    question = "I want to go to an exhibition in July. Whats on?"
    response = qa_chain({"question": question})
    store_chat(question=question, response=response)
    print(response["answer"])
    print(message_history.messages)


prompt_openai()
