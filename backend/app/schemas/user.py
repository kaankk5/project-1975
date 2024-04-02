from typing import List
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    email: EmailStr


class UserLogin(UserBase):
    password: str


class User(UserBase):
    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
