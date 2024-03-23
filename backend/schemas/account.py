from typing import List
from pydantic import BaseModel
from user import User
from trade import Trade


class AccountBase(BaseModel):
    user_id: int
    balance: float = 0.0


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int
    user: User
    trades: List[Trade] = []

    class Config:
        orm_mode = True


class AccountInDB(Account):
    pass

