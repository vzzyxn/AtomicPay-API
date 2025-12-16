import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# 1. Load the password from the .env file
load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Create the "Engine" (The connection to the vault)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Create a SessionLocal class (Each request will create its own session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class (We will use this to create our Tables later)
Base = declarative_base()

# 5. Dependency (We use this in our API to get a DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
