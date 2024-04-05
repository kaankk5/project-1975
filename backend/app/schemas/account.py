from typing import List
from pydantic import BaseModel
from app.schemas.user import User
from app.schemas.trade import Trade


class AccountBase(BaseModel):
    account_name: str
    balance: float


class AccountCreate(AccountBase):
    pass


class AccountDelete(BaseModel):
    account_name: str

class Account(AccountBase):
    id: int
    user: User
    trades: List["Trade"] = []

    class Config:
        orm_mode = True


class AccountInDB(Account):
    pass
