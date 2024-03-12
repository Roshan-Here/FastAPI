from pydantic import BaseModel

class Todo(BaseModel):
    name :str
    description :str
    compllete :bool
    
    class Config:
        json_schema_extra = {
            "example":{
                "name" : "leo",
                "description" : "anythiing about....",
                "compllete": True,
            }
        }