import asyncio
import asyncio
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate, db: AsyncSession):
        await self.user_repository.create_user(user_data, db)
        return {"message": "User signed up successfully"}

    async def get_accounts(self, user: User, db: AsyncSession):
        return await self.user_repository.get_accounts(user, db)

    async def create_account(self, user: User, db: AsyncSession):
        return await self.user_repository.create_account(user,db)
