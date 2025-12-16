from pydantic import BaseModel

# What we need to receive to create a user
class UserCreate(BaseModel):
    username: str
    initial_balance: int = 0  # Default to 0 if not provided

# What we send back to the user (Response)
class UserResponse(BaseModel):
    id: int
    username: str
    balance: int

    class Config:
        from_attributes = True

class TransactionCreate(BaseModel):
    sender_id: int
    receiver_id: int   # Changed from 'recipient_id' to match models.py
    amount: int
    idempotency_key: str

class TransactionResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int   # Changed from 'recipient_id' to match models.py
    amount: int
    idempotency_key: str

    class Config:
        from_attributes = True
