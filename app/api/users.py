# Here we put FastAPI models for users
from typing import List, Optional
from pydantic import BaseModel


class SpecificUser(BaseModel):
    user_id: str
    firstname: str
    lastname: str
    age: int
    email: str 
