from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id: str
    username: str
    mail: str
    firstname: str
    lastname: str
    type: str