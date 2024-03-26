from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import Settings
from app.models.account import Account,Base
from app.models.trade import Trade,Base
from app.models.user import User,Base



engine = create_engine(Settings.SQLALCHEMY_DATABASE_URL)
# engine = create_engine('postgresql://postgres:password@localhost:5433/new_database')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():

    Base.metadata.create_all(bind=engine)
