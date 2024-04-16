from app.repositories.user import UserRepository
from app.services.limit_order import LimitOrderService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from app.schemas.trade import TradeCreate
from app.services.authentication import AuthService, UserValidator
from app.repositories.user import User
from app.services.broker_services.broker import BrokerName
from app.services.broker_services.binance import BinanceClient
from enum import Enum


class BrokerName(Enum):
    BINANCE = 'Binance'
    KRAKEN = 'Kraken'


class TradeService:

    def __init__(self, user_repository: UserRepository, binance_service: BinanceClient):
        self.user_repository = user_repository
        self.binance_service = binance_service

    async def open_position(self, user: User, trade_create: TradeCreate, db: AsyncSession):
        market_buy: bool = await LimitOrderService.check_market_buy(trade_create)

        if market_buy:
            broker_name: BrokerName = BrokerName(trade_create.broker_name)
            if broker_name == BrokerName.BINANCE:
                status: bool = await self.binance_service.broker_side_validation(trade_create.symbol)


            elif broker_name == BrokerName.KRAKEN:
                print(62)
