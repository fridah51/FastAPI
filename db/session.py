from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

engine = create_engine("postgresql://postgres:21post@localhost:5432/tasks")
SessionLocal = sessionmaker(bind=engine, autocommit=False , autoflush=False)
conn = SessionLocal()