import json
import boto3

def lambda_handler(event, context):
    try:
        # Take numbers from event body
        body = event

        number1 = body.get('number1')
        number2 = body.get('number2')

        if number1 is None or number2 is None:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Invalid payload'})
            }

        # Calculate sum
        result = number1 + number2

        # Prepare response
        response = {
            'statusCode': 200,
            'body': json.dumps({'result': result}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }

        # Send response to SNS topic
        sns = boto3.client('sns')
        sns.publish(
            TopicArn='arn:aws:sns:eu-north-1:633172536382:saar1',
            Message=json.dumps(response)
        )

        return response

    except Exception as e:
        # Handle exceptions
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

