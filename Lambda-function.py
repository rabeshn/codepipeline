import json
import urllib.parse
import boto3

print('Loading function')

s3 = boto3.client('s3')
cw = boto3.client('cloudwatch')
bucket_name='trial-naijaboys'
s3_rsc = boto3.resource('s3')

def lambda_handler(event, context):
    obj = s3_rsc.Object(bucket_name,'askamaya.json')
    obj.put(Body=json.dumps(event))
