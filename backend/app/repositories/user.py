from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.models.account import Account
from app.utils import hash_password
from sqlalchemy import select
from fastapi import Depends, HTTPException
from app.repositories.db import get_db_session
from typing import Dict, Any, List
from app.api_constants import ACCOUNT_DELETED_MESSAGE

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
        query = select(Account).filter(Account.user_id == user.id)
        result = await db.execute(query)
        accounts: List[Account] = result.scalars().all()
        return accounts

    @staticmethod
    async def create_account(account_data: Dict[str, Any], db: AsyncSession) -> Account:
        account = Account(**account_data)
        db.add(account)
        await db.commit()
        return account

    @staticmethod
    async def get_account(account_name: str, user_id: int, db: AsyncSession) -> Account:
        query = select(Account).filter(Account.account_name == account_name, Account.user_id == user_id)
        result = await db.execute(query)
        account: Account = result.scalars().first()
        return account

    @staticmethod
    async def delete_account(account: Account, db: AsyncSession):
        await db.delete(account)
        await db.commit()
        return ACCOUNT_DELETED_MESSAGE
