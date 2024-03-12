from fastapi import FastAPI
from api.routes.todoroute import todorouter
from api.routes.studentroute import studentrouter
from api.routes.itemroute import itemrouter
from api.routes.home import home
from api.routes.userroute import userrouter

app = FastAPI()
app.include_router(home,tags=["home"])
app.include_router(todorouter,prefix="/todo",tags=["todo"])
app.include_router(studentrouter,prefix="/student",tags=["student"])
app.include_router(itemrouter,prefix="/item",tags=["item"])
app.include_router(userrouter,prefix="/user",tags=["User"])