from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/test_db"
 
# Create database engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)
 
# Create a session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# Base class for SQLAlchemy models
Base = declarative_base()
