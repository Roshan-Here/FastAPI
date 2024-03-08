from fastapi import APIRouter

from fastapi.responses import HTMLResponse

from config.database import check_db_connection

home = APIRouter()


@home.get(
    '/',
    response_class=HTMLResponse,
    responses={400:{"description":"404 Not Found"},200:{"description":"OOook"}}
    )
async def home_root():
    db_status = check_db_connection()["status"]
    # print(db_status)
    return f"""<h1>Sample Crud todo backend</h1>
    <p>Api Home page go to /docs</p>
    <p>Databse Status : {db_status}</p>
    """
