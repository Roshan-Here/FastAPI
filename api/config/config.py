# setting up digitalOcean

import os
import boto3
from dotenv import load_dotenv
from boto3 import session
from botocore.client import Config
from botocore.exceptions import ClientError

load_dotenv()

digital_ocean_bucket_id = os.environ.get("DIGITAL_OCEAN_BUCKET_ID")
digital_ocean_bucket_secret = os.environ.get("DIGITAL_OCEAN_BUCKET_SECRET")
region_name = os.environ.get("REGION_NAME")
endpoint_url = os.environ.get("ENDPOINT_URL")

print(f"{digital_ocean_bucket_id, digital_ocean_bucket_secret, region_name, endpoint_url}")

s3 = boto3.client(
    's3',
    region_name=region_name,
    aws_access_key_id=digital_ocean_bucket_id,
    aws_secret_access_key=digital_ocean_bucket_secret,
    endpoint_url=endpoint_url
    )    

try:
    # Make the API call to list objects in the S3 bucket
    response = s3.list_objects_v2(Bucket="kdev-blog")
    print("Objects in the bucket:", response)
except Exception as e:
    print("An error occurred:", e)
    

# for x in s3.buckets.all():
    # print(x.name) #-> goplege-bucket

session = session.Session()
Docean_client = session.client(
    's3',
    region_name=region_name,
    endpoint_url=endpoint_url,
    aws_access_key_id=digital_ocean_bucket_id,
    aws_secret_access_key=digital_ocean_bucket_secret,
)


# create new bucket

def create_bucket(bucket_name):
    try:
        location = {'LocationConstraint':region_name}
        Docean_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        print(f"{e}")
        return f"bucket created {False}"
    return f"bucket created {True}"        
        
        
blog = "kdev-blog"
res = create_bucket(blog)
# print(res) -> bucket created

# check if folder exist or not
def folder_exist(
    D_client,
    bucket_name="goplege-bucket",
):
    responce = D_client.list_objects_v2(bucket_name,Prefix=folder_prefix)
    return "Contents" in responce 


def list_all_datas(
    D_client,
    bucket_name="goplege-bucket",    
):
    objects = []
    paginator = D_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name)
    
    for x in page_iterator:
        print(x['Contents'])

# responce = boto3.client.list_folders(
#     AwsAccountId=digital_ocean_bucket_id,
#     NextToken=digital_ocean_bucket_secret,
#     MaxResults = 123    
# )
# print(responce)