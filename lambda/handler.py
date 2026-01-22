import json
import boto3
import os
import uuid

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ.get("TABLE_NAME")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN")

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)

    for record in event["Records"]:
        body = json.loads(record["body"])

        item = {
            "request_id": str(uuid.uuid4()),
            "payload": body
        }

        table.put_item(Item=item)

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Request Processed",
            Message=json.dumps(item)
        )

    return {
        "statusCode": 200,
        "body": "Processed messages successfully"
    }
