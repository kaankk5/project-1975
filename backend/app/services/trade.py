from app.repositories.user import UserRepository
from app.services.limit_order import LimitOrderService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from app.schemas.trade import TradeCreate
from app.services.authentication import AuthService, UserValidator
from app.repositories.user import User
from app.services.broker_services.broker_client_factory import *


class TradeService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def open_position(self, user: User, trade_create: TradeCreate, db: AsyncSession):
        market_buy: bool = await LimitOrderService.check_market_buy(trade_create)
        # Mean we have a market_buy instead of limit_order so we gonna directly buy or sell the coin
        if market_buy:
            broker: BrokerClientFactory = BrokerClientFactory.create_client(trade_create.broker_name)
            print(broker)