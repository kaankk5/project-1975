from fastapi import Depends, HTTPException
from fastapi import APIRouter
from app.services.authentication import AuthService
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.db import get_db_session
from app.api_constants import (
    POST_METHOD, LOGIN_ROUTE, STATUS_401, INVALID_USERNAME_PASSWORD_TEXT, ACCESS_KEY,
    TOKEN_TYPE_KEY,BEARER_RESPONSE_TEXT

)


class AuthController:
    def __init__(self, auth_service: AuthService):
        self.router = APIRouter()
        self.auth_service = auth_service
        self.router.add_api_route(LOGIN_ROUTE, self.login, methods=[POST_METHOD])

    async def login(self, user_login: UserLogin, db: AsyncSession = Depends(get_db_session)):
        user_authenticated = await self.auth_service.authenticate_user(user_login.username, user_login.password, db)
        if not user_authenticated:
            raise HTTPException(status_code=STATUS_401, detail=INVALID_USERNAME_PASSWORD_TEXT)
        token = self.auth_service.create_access_token(user_authenticated.id)
        return {ACCESS_KEY: token, TOKEN_TYPE_KEY: BEARER_RESPONSE_TEXT}
