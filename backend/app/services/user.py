from app.repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.models.account import Account
from app.schemas.account import AccountCreate
from app.schemas.user import UserCreate
from typing import List
from app.http_constants import MESSAGE_KEY,USER_SIGNUP_MESSAGE

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate, db: AsyncSession):
        await self.user_repository.create_user(user_data, db)
        return {MESSAGE_KEY: USER_SIGNUP_MESSAGE}

    async def get_accounts(self, user: User, db: AsyncSession) -> List[Account]:
        return await self.user_repository.get_accounts(user, db)

    async def create_account(self, user_id: int, account_create: AccountCreate, db: AsyncSession) -> Account:
        account_data = {
            "user_id": user_id,
            "account_name": account_create.account_name,
            "balance": account_create.balance,
        }
        return await self.user_repository.create_account(account_data, db)

    async def get_account_by_name(self, account_name: str, user_id: int, db: AsyncSession) -> Account:
        return await self.user_repository.get_account(account_name, user_id, db)

    async def delete_account(self, account: Account, db: AsyncSession):
        return await self.user_repository.delete_account(account, db)
