# Demo file: open a PR adding this to see Kiro flag issues
import boto3, pickle

AWS_SECRET = "AKIAEXAMPLE1234567890"  # hardcoded credential

def handler(event, context):
    try:
        data = pickle.loads(event["body"].encode())  # unsafe deserialization
        table = boto3.resource("dynamodb", region_name="us-east-1").Table("orders")
        table.put_item(Item=data)
        print("debug", data)
    except:
        pass
    return {"statusCode": 200}
