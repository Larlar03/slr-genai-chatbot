import os
import sys
import json
import boto3
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SLRChatHistory")

secrets_manager_client = boto3.client("secretsmanager")
secret_name = "OPENAI_API_KEY"
secret_response = secrets_manager_client.get_secret_value(SecretId=secret_name)
secret_value = secret_response["SecretString"]
secret_dict = json.loads(secret_value)
openai_api_key = secret_dict["OPENAI_API_KEY"]


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)


def lambda_handler(event, context):
    try:
        question = event["question"]

        if question:
            return {
                "statusCode": 200,
                "body": json.dumps(question),
            }
        else:
            return {
                "statusCode": 400,
                "body": json.dumps(
                    {"message": "Invalid request. 'question' missing in the payload."}
                ),
            }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "An error occurred."}),
        }
