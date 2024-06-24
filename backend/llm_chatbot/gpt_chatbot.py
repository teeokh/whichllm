from openai import OpenAI
import os
import json
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name):

    secret_name = secret_name
    region_name = "eu-west-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )

    except ClientError as e:
        raise e


    secret = get_secret_value_response['SecretString']
    secret=json.loads(secret)
    for key, value in secret.items():os.environ[key] = value

openai_api_key = get_secret("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Returns the usecase category based on user text input
def categorise_text(text):
    try:
        response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:whichllm-2:9cGNxEkl:ckpt-step-224",
        messages=[
            {
            "role": "system",
            "content": [
                {
                "text": "You are working for an LLM recommendation application. Your only purpose is to categorise the user's desired use case into one of several categories. The listed categories: General Knowledge, Science, Advanced Reasoning, Mathematics, Programming, Medical Knowledge, Legal Knowledge, Document Analysis, Image Analysis, Audio Processing, Video Analysis, Text Generation, Creativity, Relative User Preference, Internet Search, Wildcard. If there is no clear use case, please return 'Wildcard'.",
                "type": "text"
                }
            ]
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        category = response.choices[0].message.content
        return category
        
    except Exception as e:
        print(f"Error categorizing text: {e}")
        raise RuntimeError("Failed to categorize text")