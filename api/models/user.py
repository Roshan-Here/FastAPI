from typing import Optional

from pydantic import BaseModel,Field,EmailStr

# to create user_account
class UserModel(BaseModel):
    """_summary_
    -> get and setup password into has
    Args:
        BaseModel (_type_): _description_
    """
    username : str = Field(...)
    full_name : str = Field(...)
    email : EmailStr = Field(...)
    hashed_password : str = Field(...) # only one pass req, other checking can be done on frontend
    
    class Config:
        json_schema_extra={
            "example":{
                "username":"its_me_leo",
                "fullname":"Leo Paul",
                "email":"leo@gmail.com",
                "hashed_password":"Enter your password to be acess your acc"
            }
        }
        
class LoginModel(BaseModel):
    """_summary_
    -> steps to do..
    check if username exist in db
    check if user already logged in ? by  get_user method...

    Args:
        BaseModel (_type_): _description_
    """
    username : str = Field(...)
    password : str = Field(...)
    
    class Config:
        json_schema_extra = {
            "example":{
                "username":"your username while creating account",
                "password":"password to login"
            }
        }
        
# user update
class UserUpdateModel(BaseModel):
    """_summary_
    update usermodel, -> list of steps to do
    - check if username exist in db
    - then update the fields...

    Args:
        BaseModel (_type_): _description_
    """
    username : str = Field(...,gt=0,lt=40)
    full_name : str = Field(...)
    email : EmailStr = Field(...)
    hashed_password : str = Field(...) # only one pass req, other checking can be done on frontend
    
    class Config:
        json_schema_extra={
            "example":{
                "username":"its_me_leo",
                "fullname":"Leo Paul",
                "email":"leo@gmail.com",
                "hashed_password":"Enter your password to be acess your acc"
            }
        }