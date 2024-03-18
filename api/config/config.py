# setting up digitalOcean

import os
import shutil
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

# print(f"{digital_ocean_bucket_id, digital_ocean_bucket_secret, region_name, endpoint_url}")


s3_client = boto3.client(
    's3',
    region_name=region_name,
    endpoint_url=endpoint_url,
    aws_access_key_id=digital_ocean_bucket_id,
    aws_secret_access_key=digital_ocean_bucket_secret,
)

# try:
#     response = s3_client.list_buckets()
#     buckets = response['Buckets']
#     bucket_names = [bucket['Name'] for bucket in buckets]
#     for bucket_name in bucket_names:
#         print(bucket_name)
# except KeyError:
#     print("No buckets found.")


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
        return Docean_client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration=location)
    except ClientError as e:
        print(f"{e}")
        return f"bucket created {False}"
    # return f"bucket created {True}"        
        
        
blog = "kdev-blog"
# res = create_bucket(blog)
# print(res) #-> bucket created


# retriving list of objects in required bucketname
try:
    # Make the API call to list objects in the S3 bucket
    response = Docean_client.list_objects_v2(Bucket="kdev-blog")
    print("Objects in the bucket:", response)
except Exception as e:
    print("An error occurred:", e)
    
    
def check_upload(folder_path,req_path,bucket_name='kdev-blog',s3_client=s3_client):
    # folder_path, bucket_name="kdev-blog",s3_client=s3_client
    for roots,dirs,files in os.walk(folder_path):
        # print(roots,dirs,files)
        path_array = []
        for file in files:
            custom_path = f"{req_path}/{file}"
            local_path = os.path.join(roots,file)
            print(custom_path)
            # upload path -> Leo\Title\photo_2023-09-11_21-17-26.jpg
            s3_path = os.path.relpath(local_path,folder_path)
            print(s3_path)
            # path_array.append(custom_path)
            print(file)
            try:
                # path , bucket_name, file_name , ExtraArgs={'ACL': 'public-read'}
                # s3_client.upload_file(local_path,bucket_name,custom_path,ExtraArgs={'ACL': 'public-read'})
                download_path = f"{endpoint_url}/{custom_path}"
                path_array.append(download_path)
                # print("helloo..")
            except Exception as e:
                print(f"err : {e}")
        print(path_array)
        return path_array
    """
    upload_path = author/title/
    folder_path = media

    """

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
# f_path = os.path.join(BASE_DIR,'media')
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_URI = os.path.join(BASE_DIR,f"media")
F_PATH = os.path.join(MEDIA_URI,'Leo')
FF_PATH = os.path.join(F_PATH,'Title')
REQ_PATH = 'Leo/Title' # -> Author/Title
print(FF_PATH)
IMG_ARRAY = check_upload(folder_path=FF_PATH,req_path=REQ_PATH)
print(IMG_ARRAY)
shutil.rmtree(F_PATH)
    

def check_download(img_array,bucket_name='kdev-blog',s3_client=s3_client):
    for x in img_array:
        f_name = x.split('/')[-1]
        print(f_name)
        # try:
        #     s3_client.download_file(bucket_name,f_name,x)
        # except Exception as e:
        #     print(f"err: {e}")

# check_download(IMG_ARRAY)












bucket_list = Docean_client.list_buckets()
# print(bucket_list['Buckets'])


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