import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
mongo_uri = os.environ.get("MONGO_URL")

client = MongoClient(mongo_uri)

db = client.todo_db

collection_name = db['todo_collection']