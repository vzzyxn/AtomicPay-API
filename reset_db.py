from database import engine
from models import Base

print("Dropping old tables...")
Base.metadata.drop_all(bind=engine)

print("Creating new tables...")
Base.metadata.create_all(bind=engine)

print("Success! The database has been reset with the new columns.")
