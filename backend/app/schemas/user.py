from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
