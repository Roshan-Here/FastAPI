from fastapi import APIRouter

from models.student import StudentModel

from config.database import student_collection

from schema.schemas import retrive_student

from bson import ObjectId

# Router for Student model

studentrouter = APIRouter()

# post method
@studentrouter.post('/create')
async def create_student(data:StudentModel):
    stud = student_collection.insert_one(dict(data))
    new_student = student_collection.find_one({"_id":stud.inserted_id})
    return retrive_student(new_student)

@studentrouter.get('/detail/{id}')
async def get_student(id:str):
    student_data = student_collection.find_one({"_id":ObjectId(id)})
    # print(student_data)
    return retrive_student(student_data)

@studentrouter.get("/getall")
async def get_all_student():
    all_data = student_collection.find()
    datas = []
    for x in all_data:
        datas.append(retrive_student(x))
    return datas

@studentrouter.put("/update/{id}")
async def update_student(id:str, data:StudentModel):
    update = student_collection.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(data)})
    return retrive_student(update)

@studentrouter.delete("/delete/{id}")
async def delete_student(id:str):
    delete = student_collection.find_one({"_id":ObjectId(id)})
    if delete:
        student_collection.delete_one({"_id":ObjectId(id)})
        return True