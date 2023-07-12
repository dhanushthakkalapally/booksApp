from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

sql_username = os.environ['SQL_USERNAME']
sql_password = os.environ['SQL_PASSWORD']
sql_host = os.environ['SQL_HOST']
sql_database = os.environ['SQL_DATABASE_NAME']

SQLALCHEMY_DATABASE_URL = f"postgresql://{sql_username}:{sql_password}@{sql_host}/{sql_database}"

# creates the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# creates a session maker which manages the session of sql alchemy through which we can interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
