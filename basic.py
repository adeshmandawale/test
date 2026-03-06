import boto3
import json
import os

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.client('s3')
    bucket_name = os.environ['BUCKET_NAME']
    key = 'data.json'
    
    # Create a sample JSON data
    data = {
        "message": "Hello, World!",
        "event": event
    }
    
    # Convert the data to JSON string
    json_data = json.dumps(data)
    
    # Upload the JSON data to S3
    s3.put_object(Bucket=bucket_name, Key=key, Body=json_data)
    
    return {
        'statusCode': 200,
        'body': json_data
    }
