from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.config import Settings

# Create SQLAlchemy engine
engine = create_engine(Settings.SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class for creating session objects
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base
Base = declarative_base()