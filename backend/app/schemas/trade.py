from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from account import Account
from datetime import datetime


class TradeBase(BaseModel):
    account_id: int
    symbol: str
    leverage: int
    timestamp: datetime
    is_long: bool


class TradeCreate(TradeBase):
    pass


class Trade(TradeBase):
    id: int
    profit: Optional[float] = None
    roi: Optional[float] = None
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None
    account: Account

    class Config:
        orm_mode = True


class TradeInDB(Trade):
    pass
