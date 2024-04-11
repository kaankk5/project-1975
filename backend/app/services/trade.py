from app.repositories.user import UserRepository
from app.services.limit_order import LimitOrderService
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Request
from app.schemas.trade import TradeCreate


class TradeService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def open_position(self, request: Request, trade_create: TradeCreate, db: AsyncSession):
        market_buy: bool = await LimitOrderService.check_market_buy(trade_create)
        print(request.headers)

