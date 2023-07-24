import os
import sys
import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("SLRChatHistory")

secrets_manager_client = boto3.client("secretsmanager")
secret_name = "OPENAI_API_KEY"
response = secrets_manager_client.get_secret_value(SecretId=secret_name)
secret_value = response["SecretString"]


def lambda_handler(event, context):
    try:
        question = event.get("body")

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
