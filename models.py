from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    # We store balance as an Integer (cents) to avoid floating point math errors
    # Example: $10.00 is stored as 1000
    balance = Column(Integer, default=0)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer) # In cents
    status = Column(String, default="success") # success, failed, pending
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    
    # Added the missing column here
    idempotency_key = Column(String, unique=True, index=True)
