from fastapi import FastAPI

from routes.todoroute import todorouter
from routes.studentroute import studentrouter
from routes.home import home

app = FastAPI()
app.include_router(todorouter,prefix="/todo",tags=["todo"])
app.include_router(studentrouter,prefix="/student",tags=["student"])
app.include_router(home,tags=["home"])