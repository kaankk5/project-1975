from app.models.base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship




class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    symbol = Column(String, nullable=False)
    leverage = Column(Integer, nullable=False)
    profit = Column(Float, nullable=True)
    current_price = Column(Float, nullable=True)
    roi = Column(Float, nullable=True)
    timestamp = Column(DateTime, nullable=False)
    is_long = Column(Boolean, nullable=False)
    buying_price = Column(Float, nullable=True)
    selling_price = Column(Float, nullable=True)
    on_going = Column(Boolean, default=False)
    account = relationship("Account", back_populates="trades")






