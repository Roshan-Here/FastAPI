import os
from fastapi import APIRouter,Form,File,UploadFile

from config.database import item_collection,fs,MEDIA_URI
from models.items import ItemModel
from schema.schemas import retrive_items

itemrouter = APIRouter()


@itemrouter.post('/create')
async def create_item(
    name:str=Form(...),
    description:str=Form(...),
    images:UploadFile = File(None),
    ):
    if images:
        contents = await images.read()
        file_name = images.filename
        location = os.path.join(MEDIA_URI,f'{file_name}')
        print(location)
        with open(location,"wb") as f:
            f.write(contents)
            
    item_dict = {
        "name":name,
        "description":description,
        "images_url":location
    }
    item = item_collection.insert_one(item_dict)
        
        
        # nice = fs.put(contents,file_name)
        # print(nice)
        # data.images = location
        # print(data)
    # store location of where media stored/ 
    # one way
    # items = item_collection.insert_one({dict(data)}) 
    # store image in instance
    # ItemMoel.image = instance obj id
    # retrive it by find_one({"_id":nice.id})
    
    