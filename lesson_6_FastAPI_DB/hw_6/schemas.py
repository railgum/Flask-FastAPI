from pydantic import BaseModel


class OrderBase(BaseModel):
    order_status: str


class OrderCreate(OrderBase):
    id: int


class Order(OrderBase):
    order_date: str
    order_status: str
    user_id: int
    product_id: int


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    id: int
    password: str


class User(UserBase):
    firstname: str
    lastname: str
    orders: list[Order] = []


class ProductBase(BaseModel):
    title: str


class ProductCreate(ProductBase):
    id: int


class Product(ProductBase):
    description: str | None = None
    price: float
    orders: list[Order] = []
