from fastapi import APIRouter
from app.services.trade import TradeService
from app.services.authentication import AuthService, UserValidator
from app.api_constants import USER_CREATED_MESSAGE, MESSAGE_KEY, GET_METHOD, HOME_ROUTE
from app.repositories.db import get_db_session
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.trade import TradeCreate


class TradeController:

    def __init__(self, trade_service: TradeService, auth_service: AuthService):
        self.trade_service = trade_service
        self.auth_service = auth_service
        self.router = APIRouter()
        self.add_routes()

    async def open_position(self, trade_create: TradeCreate, db: AsyncSession = Depends(get_db_session)):
        # This is the place where i change my monolith system into micro ones :d
        # self.trade_service.open_postion
        return {"message": "+Askim cekimdeyim? -Ne cekimi? +31"}

    def add_routes(self):
        self.router.add_api_route(HOME_ROUTE, self.open_position, methods=[GET_METHOD],
                                  dependencies=[Depends(UserValidator())])
