from fastapi import APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from app.services.user import UserService
from app.services.authentication import AuthService, UserValidator
from app.schemas.user import UserCreate, UserLogin
from app.repositories.db import get_db_session
from app.models.user import User


class UserController:

    def __init__(self, user_service: UserService, auth_service: AuthService):
        self.user_service = user_service
        self.router = APIRouter()
        self.auth_service = AuthService
        self.add_routes()

    def add_routes(self):
        self.router.add_api_route("/register", self.signup, methods=["POST"])
        self.router.add_api_route("/protected", self.protected_endpoint, methods=["POST", "GET"])

    async def signup(self, user_data: UserCreate, db: AsyncSession = Depends(get_db_session)):
        await self.user_service.create_user(user_data, db)
        return {"message": "31111"}

    async def protected_endpoint(self,current_user: User = Depends(UserValidator())):
        pass



