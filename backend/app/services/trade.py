from app.repositories.user import UserRepository
from app.services.limit_order import LimitOrderService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from app.schemas.trade import TradeCreate
from app.services.authentication import AuthService, UserValidator
from app.repositories.user import User
from app.services.broker_services.broker_factory import BrokerFactory
from app.services.broker_services.deneme import annesi


class TradeService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def open_position(self, user: User, trade_create: TradeCreate, db: AsyncSession):
        market_buy: bool = await LimitOrderService.check_market_buy(trade_create)
        # Mean we have a market_buy instead of limit_order so we gonna directly buy or sell the coin.
        # Make ws connection to whatever broker. Pass those prices to runtime thr mq. Then from runtime calculate
        # roi and profit stream it back to my website.
        # For sure runtime has to be different service.So in best case sceniro im gonna have 2 microservices.
        if market_buy:
            print(annesi)
            print(31)

        # Here it gets little complicated.
        # I should still pass the data to mq. But first we should wait to price hit whatever limit order we have.
        #Then open trade.add it db and so on.
        # So i might need an intermediate service to check does prices not sure yet.Probably this should be
        # Different service like runtime.
        else:
            print()