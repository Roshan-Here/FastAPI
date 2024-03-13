from fastapi import APIRouter,Form
from fastapi.responses import JSONResponse
from api.models.user import UserModel
from api.jwt.settings import pwd_context
from api.config.database import user_collection

userrouter = APIRouter()


@userrouter.post('/create')
async def user_create(data:UserModel):
    # hashing the password
    password = pwd_context.hash(data.hashed_password)
    data.hashed_password = password
    print(password)
    # check if user exist in db
    try:
        users = user_collection.find()
        if data.username in users:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message":"username already exist in db, use different username"
                }
            )
        else:
            user_collection.insert_one(dict(data))
    except Exception as e:
        return JSONResponse(
            status_code = 500,
            content = {
                "message":f"user collection issue {e}"
            }
        )
            
@userrouter.get("/login")
async def get_login_token(
    username:str=Form(...),
    password:str=Form(...),
):
    """
        Generate and return acess,refresh token for login success 
    """