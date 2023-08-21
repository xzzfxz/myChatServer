from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    account: str
    username: Optional[str] = None
    phone: Optional[str] = None


class UserInDB(User):
    password: str
