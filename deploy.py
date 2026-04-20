import boto3
import os

s3 = boto3.client('s3')

BUCKET_NAME = 'github-automoted-action-dev-22'

# Upload all image files from repo
for file in os.listdir():
    if file.endswith(('.jpg', '.jpeg', '.png')):
        print(f"Uploading {file}...")
        s3.upload_file(file, BUCKET_NAME, file)
