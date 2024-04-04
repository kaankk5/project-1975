from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Request
from app.services.user import UserService
from app.services.authentication import AuthService, UserValidator
from app.schemas.user import UserCreate, UserLogin
from app.repositories.db import get_db_session
from app.models.user import User
from app.models.account import Account
from app.repositories.user import UserRepository
from app.schemas.account import AccountCreate


class UserController:

    def __init__(self, user_service: UserService, auth_service: AuthService):
        self.user_service = user_service
        self.auth_service = auth_service
        self.router = APIRouter()
        self.add_routes()

    def add_routes(self):
        self.router.add_api_route("/register", self.signup, methods=["POST"])
        self.router.add_api_route("/accounts", self.list_accounts, methods=["GET"],
                                  dependencies=[Depends(UserValidator())])
        self.router.add_api_route("/accounts", self.post_account, methods=["POST"],
                                  dependencies=[Depends(UserValidator())])

    async def signup(self, user_data: UserCreate, db: AsyncSession = Depends(get_db_session)):
        await self.user_service.create_user(user_data, db)
        return {"message": "User created successfully"}

    async def list_accounts(self, request: Request, db: AsyncSession = Depends(get_db_session)):
        user: User = await self.auth_service.get_current_user(request, db)
        accounts = await self.user_service.get_accounts(user, db)

        return {"message": accounts}

    async def post_account(self, request: Request, account_create: AccountCreate, db: AsyncSession = Depends(get_db_session)):

        print('calisti')
        print(account_create)



