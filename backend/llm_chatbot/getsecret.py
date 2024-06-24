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
    print(os.getenv(secret_name))