from typing import Optional

from pydantic import BaseModel,Field


class ItemModel(BaseModel):
    name : str = Field(...)
    description :str = Field(...)
    images_url : Optional[str] = None
    
    class Config:
        json_schema_extra={
            "example":{
                "name":"item name",
                "description":"small description about the item",
                "images":"upload image of item",
            }
        }
    