from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.models.account import Account

from app.utils import hash_password
from sqlalchemy import select
from fastapi import Depends, HTTPException
from app.repositories.db import get_db_session


class UserRepository:

    @staticmethod
    async def create_user(user_data: UserCreate, db: AsyncSession) -> User:
        hashed_password: str = hash_password(user_data.password)
        user: User = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
        db.add(user)
        await db.commit()
        return user

    @staticmethod
    async def get_by_username(username: str, db: AsyncSession) -> User:
        query = select(User).filter(User.username == username)
        result = await db.execute(query)
        user: User = result.scalars().first()
        return user

    @staticmethod
    async def get_by_id(user_id: int, db: AsyncSession) -> User:
        query = select(User).filter(User.id == user_id)
        result = await db.execute(query)
        user: User = result.scalars().first()
        return user

    @staticmethod
    async def get_accounts(user: User, db: AsyncSession) -> User:
        query = select(User).filter(Account.user_id == user.id)
        result = await db.execute(query)
        accounts: Account = result.scalars().all()
        print(accounts)
        return accounts

    async def create_account(self, user: User, db: AsyncSession):
        account = Account(user_id=user.id)  # Assuming Account model has a user_id field
        db.add(account)
        await db.commit()
        return account

