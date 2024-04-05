from sqlalchemy import Column, ForeignKey, Integer, Float, String
from sqlalchemy.orm import relationship
from app.models.base import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    account_name = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=100.0)
    total_roi = Column(Float, nullable=True, default=0.0)
    total_profit = Column(Float, nullable=True, default=0.0)
    trades = relationship("Trade", back_populates="account")
    user = relationship("User", back_populates="accounts")

    def __str__(self):
        return f"Account(id={self.id}, user_id={self.user_id}, account_name='{self.account_name}', balance={self.balance})"
