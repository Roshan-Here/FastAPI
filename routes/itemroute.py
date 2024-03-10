import os, shutil
from fastapi import APIRouter,Form,File,UploadFile,HTTPException
from fastapi.responses import JSONResponse
from config.database import item_collection,fs,MEDIA_URI
from models.items import ItemModel
from schema.schemas import retrive_items

from bson import ObjectId
itemrouter = APIRouter()


@itemrouter.post('/create')
async def create_item(
    name:str=Form(...),
    description:str=Form(...),
    images:list[UploadFile] = File(None),
    ):
    print(type(name))
    image_array = []
    if images:
        for image in images:
            contents = await image.read()
            file_name = str(image.filename)
            location = os.path.join(MEDIA_URI,f"{name}")
            
            try:
                os.makedirs(location, exist_ok=True)
                org_location = os.path.join(location,f'{file_name}')
                with open(org_location,"wb") as f:
                    f.write(contents)
                    image_array.append(org_location)
            except Exception as e:
                print(f"eror while creating dir {e}")

            
        print(location)
        print(org_location)
    item_dict = {
        "name":name,
        "description":description,
        "images_url": image_array,
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
    
    
    
@itemrouter.get('/getall')
async def getall_item():
    items = item_collection.find()
    datas = []
    for x in items:
        datas.append(retrive_items(x))
    return datas


@itemrouter.delete("/delete/{id}")
def item_delete(id:str):
    # check if id exist
    check_id_exist = item_collection.db.find_one({"_id":id})
    if check_id_exist:
        item_collection.delete_one({"_id":id})
    else:
        raise HTTPException(status_code=400,detail="id not found")
    return JSONResponse(
        status_code=200,
        content={
            "message":"Sucessfully deletedd the item!"
        }
    )
    
@itemrouter.delete("/deleteall")
def deleteall_item():
    items = item_collection.find()
    for x in items:
        # print(x["_id"])
        try:
            del_dir = os.path.join(MEDIA_URI,x["name"])
            print(del_dir)
            if os.path.exists(del_dir):
                shutil.rmtree(del_dir)
            else:
                print("folder not found !")
        except Exception as e:
            raise HTTPException(status_code=400,detail=f"error {e}")
        item_collection.delete_one({"_id":x["_id"]})
    return JSONResponse(
    status_code=200,
    content={
        "message":"deleted all items !"
        }
    )
    
@itemrouter.get("/get/{id}")
async def get_by_id(id:str):
    item = item_collection.find_one({"_id":id})
    if item:
        return retrive_items(item)
    else:
        JSONResponse(
            status_code=400,
            content={
                "message":"unable to find item !"
            }
        )
        
@itemrouter.put("/update/{id}")
async def update_item(
    id:str,
    name:str=Form(None),
    description:str=Form(None),
    images_url:list[UploadFile]=File(None)
    ):
    item = item_collection.find_one({"_id":ObjectId(id)})
    if not name:
        name = item["name"]
    if not description:
        description = item["description"]
    if not images_url:
        images_url = item["images_url"]
    
            
    image_array = []
    if images_url:
        for image in images_url:
            contents = await image.read()
            file_name = str(image.filename)
            location = os.path.join(MEDIA_URI,f"{name}")
            
            try:
                os.makedirs(location, exist_ok=True)
                org_location = os.path.join(location,f'{file_name}')
                with open(org_location,"wb") as f:
                    f.write(contents)
                    image_array.append(org_location)
            except Exception as e:
                print(f"eror while creating dir {e}")

            
        print(location)
        print(org_location)
    item_dict = {
        "name":name,
        "description":description,
        "images_url": image_array,
    }
    item = item_collection.update_one({"_id":ObjectId(id)},{"$set":item_dict})
    new_item = item_collection.find_one({"_id":ObjectId(id)})
    return retrive_items(new_item)