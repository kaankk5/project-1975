from base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from enum import Enum

class LimitOrderType(str,Enum):
    LIMIT_BUY ='LIMIT_BUY'
    LIMIT_SELL ='LIMIT_BUY'



class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    symbol = Column(String, nullable=False)
    leverage = Column(Integer, nullable=False)
    buying_price = Column(Float, nullable=True)
    selling_price = Column(Float, nullable=True)
    profit = Column(Float, nullable=True)
    current_price = Column(Float, nullable=True)
    roi = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)
    is_long = Column(Boolean, nullable=False)
    is_short = Column(Boolean, nullable=False)
    account = relationship("Account", back_populates="trades")

