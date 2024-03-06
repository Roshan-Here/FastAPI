import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

load_dotenv()
mongo_uri = os.environ.get("MONGO_URL")

client = MongoClient(mongo_uri)

db = client.todo_db

collection_name = db['todo_collection']

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