from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
# from app.schemas.account import Account
from datetime import datetime


class TradeBase(BaseModel):
    account_name: str
    symbol: str
    leverage: Optional[int]
    timestamp: datetime
    is_long: bool


class TradeCreate(TradeBase):
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None

    @validator("buying_price")
    def validate_buying_price(cls, v, values):
        if v is not None and values.get("selling_price") is not None:
            raise ValueError("Only one of buying_price or selling_price can be provided")
        return v

    @validator("selling_price")
    def validate_selling_price(cls, v, values):
        if v is not None and values.get("buying_price") is not None:
            raise ValueError("Only one of buying_price or selling_price can be provided")
        return v


class Trade(TradeBase):
    id: int
    profit: Optional[float] = None
    roi: Optional[float] = None
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None

    # account: Account

    class Config:
        orm_mode = True


class TradeInDB(Trade):
    pass
