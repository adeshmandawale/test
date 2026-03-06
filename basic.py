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

 #Additionally, you can add error handling to ensure that any issues with the S3 upload are properly logged and handled. Here's an updated version of the code with error handling: