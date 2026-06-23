import json

def lambda_handler(event, context):

    response = {
        "project": "Cloud Services API",
        "services": [
            {
                "name": "Amazon S3",
                "purpose": "Object Storage"
            },
            {
                "name": "AWS Lambda",
                "purpose": "Serverless Computing"
            },
            {
                "name": "Amazon EC2",
                "purpose": "Virtual Servers"
            },
            {
                "name": "Amazon RDS",
                "purpose": "Managed Database"
            }
        ],
        "status": "success"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response, indent=4)
    }