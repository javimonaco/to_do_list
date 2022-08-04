from pydantic import BaseModel
from datetime import datetime
from typing import Text
from uuid import uuid4

class Task(BaseModel):
    id: str
    id_user: str
    title: str
    summary: Text
    dateIni: datetime = datetime.now()
    dateEnd: datetime
    completed: bool = False
    deleted: bool = False

class User(BaseModel):
    id: str
    name: str
    firstname: str
    lastname: str
    email: str
    password: str
    deleted: bool = False
