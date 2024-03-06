from fastapi import APIRouter

from models.todos import Todo

from config.database import collection_name

from schema.schemas import list_all_serializer,single_serial

from bson import ObjectId

router = APIRouter()


# Get Request
@router.get('/')
async def get_todo():
    todos = list_all_serializer(collection_name.find())
    return todos

# Get Post Request
@router.post('/create')
async def create_todo(todo:Todo):
    collection_name.insert_one(dict(todo))