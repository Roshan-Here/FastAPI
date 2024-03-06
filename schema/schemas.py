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