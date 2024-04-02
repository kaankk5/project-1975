from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from app.config import Settings
from app.models.account import Account, Base
from app.models.trade import Trade, Base
from app.models.user import User, Base

#engine and session
async_engine = create_async_engine(Settings.SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)



async def get_db_session():
    async with async_session() as session:
        yield session

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
