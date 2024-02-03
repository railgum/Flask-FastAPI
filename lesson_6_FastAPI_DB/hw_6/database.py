import databases
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./lesson_6_FastAPI_DB/hw_6/instance/hw_6.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()


users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('firstname', sqlalchemy.String(32)),
    sqlalchemy.Column('lastname', sqlalchemy.String(64)),
    sqlalchemy.Column('email', sqlalchemy.String(128)),
    sqlalchemy.Column('password', sqlalchemy.String(32)),
)

products = sqlalchemy.Table(
    'products',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('title', sqlalchemy.String(32)),
    sqlalchemy.Column('description', sqlalchemy.String(512)),
    sqlalchemy.Column('price', sqlalchemy.Float)
)

orders = sqlalchemy.Table(
    'orders',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('user_id', sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('order_id', sqlalchemy.ForeignKey('orders.id')),
    sqlalchemy.Column('order_date', sqlalchemy.String(16)),
    sqlalchemy.Column('order_status', sqlalchemy.String(16))
)
