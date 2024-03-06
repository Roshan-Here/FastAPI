from fastapi import APIRouter

from fastapi.responses import HTMLResponse

from models.todos import Todo

from config.database import collection_name, check_db_connection

from schema.schemas import list_all_serializer,single_serial

from bson import ObjectId

router = APIRouter()

@router.get(
    '/',
    response_class=HTMLResponse,
    responses={400:{"description":"404 Not Found"}, 200:{"description":"Oook"}},
    tags=["root"],
    )
async def main_home():
    db_status = check_db_connection()["status"]
    # print(db_status)
    return f"""<h1>Sample Crud todo backend</h1>
    <p>Api Home page go to /docs</p>
    <p>Databse Status : {db_status}</p>
    """


# Get Request
@router.get('/todo')
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