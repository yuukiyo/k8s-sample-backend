from flask import Flask                           
import boto3
import json
import traceback
import sys
import os
import decimal
from aws_xray_sdk.core import xray_recorder, patch_all

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

ddb = boto3.resource('dynamodb')
table = ddb.Table('appmesh_sample_message')
app = Flask(__name__)                             
patch_all()

@app.route('/')
def hello_world():                                
    return '{"message": "Hello K8s!"}'

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=True)
