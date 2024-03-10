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
    print(type(name))
    if images:
        contents = await images.read()
        file_name = str(images.filename)
        location = os.path.join(MEDIA_URI,f"{name}")
        
        try:
            os.makedirs(location, exist_ok=True)
            org_location = os.path.join(location,f'{file_name}')
            with open(org_location,"wb") as f:
                f.write(contents)
        except Exception as e:
            print(f"eror while creating dir {e}")

            
        print(location)
        print(org_location)
    item_dict = {
        "name":name,
        "description":description,
        "images_url": org_location,
    }
    item = item_collection.insert_one(item_dict)
    new_item = item_collection.find_one({"_id":item.inserted_id})
    return retrive_items(new_item)
        
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
    
    
    
