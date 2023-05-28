import json

def lambda_handler(event, context):
    # take the numbers from the event body
    body = json.loads(event['body'])
    number1 = body.get('number1')
    number2 = body.get('number2')

    if number1 is None or number2 is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid payload'})
        }

    # calculate sum
    result = number1 + number2

    # prepare response
    response = {
        'statusCode': 200,
        'body': json.dumps({'result': result}),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

    return response
