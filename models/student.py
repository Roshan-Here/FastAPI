from typing import Optional

from pydantic import EmailStr,BaseModel,Field


class StudentModel(BaseModel):
    fullname : str = Field(...)
    email :EmailStr = Field(...)
    course_of_study : str = Field(...)
    year :int = Field(...,gt=0,lt=9)
    gpa : float = Field(..., le=4.0)
    
    class Config:
        json_schema_extra = {
            "exaple":{
                "fullname":"Leo paul",
                "email":"leopaul@gmail.com",
                "course_of_study":"CSE",
                "year":4,
                "gpa":"3.5",
            }
        }