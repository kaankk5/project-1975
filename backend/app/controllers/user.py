from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Request, status
from app.services.user import UserService
from app.services.authentication import AuthService, UserValidator
from app.schemas.user import UserCreate, UserLogin
from app.repositories.db import get_db_session
from app.models.user import User
from app.models.account import Account
from app.schemas.account import AccountCreate, AccountDelete
from app.api_constants import (
    ACCOUNT_NOT_FOUND_MESSAGE, MESSAGE_KEY, ACCOUNT_DELETED_MESSAGE, USER_CREATED_MESSAGE,
    STATUS_404, REGISTER_ROUTE, ACCOUNTS_ROUTE, ACCOUNTS_BY_NAME_ROUTE,
    GET_METHOD, POST_METHOD, PUT_METHOD, DELETE_METHOD

)


class UserController:

    def __init__(self, user_service: UserService, auth_service: AuthService):
        self.user_service = user_service
        self.auth_service = auth_service
        self.router = APIRouter()
        self.add_routes()

    async def signup(self, user_data: UserCreate, db: AsyncSession = Depends(get_db_session)):
        user: User = await self.user_service.create_user(user_data, db)
        return {MESSAGE_KEY: USER_CREATED_MESSAGE}

    async def list_accounts(self, request: Request, db: AsyncSession = Depends(get_db_session)):
        user: User = await self.auth_service.get_current_user(request, db)
        accounts = await self.user_service.get_accounts(user, db)
        return accounts, status.HTTP_201_CREATED

    async def post_account(self, request: Request, account_create: AccountCreate,
                           db: AsyncSession = Depends(get_db_session),
                           ):
        user: User = await self.auth_service.get_current_user(request, db)
        account: Account = await self.user_service.create_account(user.id, account_create, db)

        return account, status.HTTP_201_CREATED

    async def get_account(self, request: Request, account_name: str, db: AsyncSession = Depends(get_db_session)):
        user: User = await self.auth_service.get_current_user(request, db)
        account: Account = await self.user_service.get_account_by_name(account_name, user.id, db)
        if account:
            return account
        else:
            return {MESSAGE_KEY: ACCOUNT_NOT_FOUND_MESSAGE}, status.HTTP_404_NOT_FOUND

    async def delete_account(self, request: Request, account_data: AccountDelete,
                             db: AsyncSession = Depends(get_db_session)):
        return await self.delete_account_common(request, account_data=account_data, db=db)

    async def delete_account_by_name(self, request: Request, account_name: str,
                                     db: AsyncSession = Depends(get_db_session)):
        return await self.delete_account_common(request, account_name=account_name, db=db)

    async def delete_account_common(self, request: Request, account_name: str = None,
                                    account_data: AccountDelete = None,
                                    db: AsyncSession = Depends(get_db_session)):
        user: User = await self.auth_service.get_current_user(request, db)

        if account_data:
            account_name = account_data.account_name

        account: Account = await self.user_service.get_account_by_name(account_name, user.id, db)

        if account:
            await self.user_service.delete_account(account, db)
            return {MESSAGE_KEY: ACCOUNT_DELETED_MESSAGE}, status.HTTP_200_OK
        else:
            return {MESSAGE_KEY: ACCOUNT_NOT_FOUND_MESSAGE}, status.HTTP_404_NOT_FOUND

    def add_routes(self):
        self.router.add_api_route(REGISTER_ROUTE, self.signup, methods=[POST_METHOD])
        self.router.add_api_route(ACCOUNTS_ROUTE, self.list_accounts, methods=[GET_METHOD],
                                  dependencies=[Depends(UserValidator())])
        self.router.add_api_route(ACCOUNTS_ROUTE, self.post_account, methods=[POST_METHOD],
                                  dependencies=[Depends(UserValidator())])

        self.router.add_api_route(ACCOUNTS_BY_NAME_ROUTE, self.get_account, methods=[GET_METHOD],
                                  dependencies=[Depends(UserValidator())])

        self.router.add_api_route(ACCOUNTS_BY_NAME_ROUTE, self.delete_account_by_name, methods=[DELETE_METHOD],
                                  dependencies=[Depends(UserValidator())])

        self.router.add_api_route(ACCOUNTS_ROUTE, self.delete_account, methods=[DELETE_METHOD],
                                  dependencies=[Depends(UserValidator())])
