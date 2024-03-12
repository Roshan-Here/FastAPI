import os
from dotenv import load_dotenv

from passlib.context import CryptContext
load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY") 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30    

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")