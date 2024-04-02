from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, User
from app.repositories.db import get_db_session
from app.utils import hash_password, verify_password, set_password


# router = APIRouter(prefix='/auth')
#
#
# class TradeController:
#     def __init__(self, trade_service: trade_service, db: AsyncSession):
#         self.trade_service = trade_service
#         self.db = db
#
#
#     @router.post("/")
#     async def open_trade(self, user_data: UserCreate, db: AsyncSession = Depends(get_db_session)):
#         pass
#
#         # return await self.user_service.create_user(user_data, db)
# #        Status code
#

