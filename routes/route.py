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
    
    
# Set Put Request
@router.put('/update/{id}')
async def update_todo(id:str,todo:Todo):
    # override what already on db
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    
# Delete Request
@router.delete('/delete/{id}')
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})