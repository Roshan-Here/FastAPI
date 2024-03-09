from typing import Optional 

from pydantic import BaseModel,Field

class ItemModel(BaseModel):
    name : str : Field(...)
    description :str :Field(...)
    images : Optional[str] = None