# serializer setup like django

def single_serial(todo) -> dict:
    """single retrival

    Args:
        passing the todo Model

    Returns:
        data of specified id
    """
    return{
        "id": str(todo['_id']),
        "name": todo['name'],
        "description": todo['description'],
        "complete": todo['compllete']
    }
    
    
def list_all_serializer(todos)->dict:
    """list all the datas

    Args:
        pass the entire data model

    Returns:
        returns dict by using single_serial function by passing each model
    """
    return[
        single_serial(todo) for todo in todos
    ]
    
def retrive_student(student)->dict:
    return{
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study" : student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"], 
    }
    
    
def retrive_items(item)->dict:
    # for x in item["images_url"]:
    #     print(x)
    return{
        "id" : str(item["_id"]),
        "name": item["name"],
        "description": item["description"],
        "images_url": item["images_url"],
    }