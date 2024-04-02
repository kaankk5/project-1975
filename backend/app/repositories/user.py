from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.utils import hash_password
from sqlalchemy import select
from fastapi import Depends
from app.repositories.db import get_db_session


class UserRepository:

    async def create_user(self, user_data: UserCreate, db: AsyncSession) -> User:
        print('db: ', db)

        hashed_password: str = hash_password(user_data.password)
        user: User = User(username=user_data.username, email=user_data.email, hashed_password=hashed_password)
        db.add(user)
        await db.commit()
        return user

    async def get_by_username(self, username: str, db: AsyncSession) -> User:
        query = select(User).filter(User.username == username)
        result = await db.execute(query)
        user: User = result.scalars().first()
        return user

    async def get_by_id(self, user_id: int, db: AsyncSession = Depends(get_db_session)) -> User:
        pass







        # user: User = User(username='deneme sonucu', email='deneme@gmail.com', hashed_password='deneme')
        # db.add(user)
        # await db.commit()
        # return user

# user = await db.execute(User.select().where(User.username == username))
# return user.scalar_one_or_none()
