

import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'github-automoted-action-dev-22', 'index.html')
