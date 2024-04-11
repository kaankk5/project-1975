from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from datetime import datetime
from app.api_constants import (
    BUY_OR_SELL_ERROR, BUYING_PRICE,SELLING_PRICE
)



class TradeBase(BaseModel):
    account_name: str
    symbol: str
    leverage: Optional[int]
    timestamp: datetime
    is_long: bool
    broker_name: str


class TradeCreate(TradeBase):
    buying_price: Optional[float] = None
    selling_price: Optional[float] = None

    @validator("buying_price")
    def validate_buying_price(cls, v, values):
        if v is not None and values.get(SELLING_PRICE) is not None:
            raise ValueError(BUY_OR_SELL_ERROR)
        return v

    @validator("selling_price")
    def validate_selling_price(cls, v, values):
        if v is not None and values.get(BUYING_PRICE) is not None:
            raise ValueError(BUY_OR_SELL_ERROR)
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
