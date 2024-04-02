from fastapi import Depends, HTTPException
from fastapi import APIRouter
from app.services.authentication import AuthService
from app.schemas.user import UserCreate, UserLogin
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.db import get_db_session


class AuthController:
    def __init__(self, auth_service: AuthService):
        self.router = APIRouter()
        self.auth_service = auth_service
        self.router.add_api_route("/login", self.login, methods=["POST"])

    async def login(self, user_login: UserLogin, db: AsyncSession = Depends(get_db_session)):
        user_authenticated = await self.auth_service.authenticate_user(user_login.username, user_login.password, db)
        if not user_authenticated:
            raise HTTPException(status_code=401, detail="Invalid username or password")
        token = self.auth_service.create_access_token(user_authenticated.id)
        return {"access_token": token, "token_type": "bearer"}

