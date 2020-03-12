from flask import Flask                           
import boto3
import json
import traceback
import sys
import os
import decimal
from aws_xray_sdk.core import xray_recorder, patch_all

app = Flask(__name__)                             
patch_all()

@app.route('/')
def hello_world():                                
    return '{"message": "Hello K8s2!"}'

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=True)
