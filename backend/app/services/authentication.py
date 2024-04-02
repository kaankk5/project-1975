from app.repositories.user import UserRepository
from app.models.user import User
from app.schemas.user import UserLogin
from app.utils import create_access_token, decode_jwt_token
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, Request, Depends
from app.repositories.db import get_db_session


class UserValidator:
    def __init__(self, db: AsyncSession = Depends(get_db_session)):
        self.db = db

    async def __call__(self, request: Request):
        print(self.db)
        user_service = AuthService()
        return await user_service.get_current_user(request)


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    async def authenticate_user(self, username: str, password: str, db: AsyncSession) -> User:
        user: User = await self.user_repository.get_by_username(username, db)
        if not user or not user.verify_password(password):
            return None
        return user






    async def get_current_user(self, request: Request):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=401, detail="Authorization header is missing")

        try:
            token = token.split("Bearer ")[1]  # Extract the token from the "Bearer" token type
            payload = decode_jwt_token(token)
            user_id: int = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid token")

            print('user_id: ', user_id)
            user = await self.user_repository.get_by_id(user_id)
            print('returned user ', user)

            if user is None:
                raise HTTPException(status_code=401, detail="User not found")
            return user
        except Exception as e:
            raise HTTPException(status_code=401, detail="Could not validate credentials")

    def create_access_token(self, user_id: int) -> str:
        return create_access_token(user_id)
