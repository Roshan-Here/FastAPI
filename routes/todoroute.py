from fastapi import APIRouter

from fastapi.responses import HTMLResponse

from models.todos import Todo

from config.database import collection_name, check_db_connection

from schema.schemas import list_all_serializer,single_serial

from bson import ObjectId

todorouter = APIRouter()


# Get Request
@todorouter.get('/todo')
async def get_todo():
    todos = list_all_serializer(collection_name.find())
    return todos

# Get Post Request
@todorouter.post('/create')
async def create_todo(todo:Todo):
    collection_name.insert_one(dict(todo))
    
    
# Set Put Request
@todorouter.put('/update/{id}')
async def update_todo(id:str,todo:Todo):
    # override what already on db
    collection_name.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(todo)})
    
# Delete Request
@todorouter.delete('/delete/{id}')
async def delete_todo(id:str):
    collection_name.find_one_and_delete({"_id":ObjectId(id)})
    
