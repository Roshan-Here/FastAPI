import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import gridfs

load_dotenv(find_dotenv())
mongo_uri = os.environ.get("MONGO_URL")

client = MongoClient(mongo_uri)

db = client.todo_db

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_URI = os.path.join(BASE_DIR,f"media")
print(MEDIA_URI)

collection_name = db['todo_collection'] #to store todo datas
student_collection = db['student_collection'] #to store student datas
item_collection = db["item_collection"] #to store item datas
user_collection = db['user_collection'] #to store user datas

# file store in mongodb // not using
# fs = gridfs.GridFS(db)
# print(fs) 

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def check_db_connection():
    try:
        db.command("ismaster")
        # print(wow)
        return {"status":"Database Connected"}
    except ServerSelectionTimeoutError as e:
        return{
            "status":"Database Conneciton failed",
            "exception":str(e)
            }