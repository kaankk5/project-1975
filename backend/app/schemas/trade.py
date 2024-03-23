from pydantic import BaseModel,Field
from account import Account
from datetime import datetime


class TradeBase(BaseModel):
    account_id: int
    symbol: str
    leverage: int
    buying_price: float
    selling_price: float
    timestamp: datetime
    is_long: bool
    is_short: bool

class TradeCreate(TradeBase):
    pass

class TradeUpdate(TradeBase):
    pass

class TradeInDB(BaseModel):
    id: int
    account_id: int
    symbol: str
    leverage: int
    buying_price: float
    selling_price: float
    timestamp: datetime
    is_long: bool
    is_short: bool
    roi: float = Field(..., alias="calculated_roi")
    profit: float = Field(..., alias="calculated_profit")