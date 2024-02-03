from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from fastapi import FastAPI
from typing import List

DATABASE_URL = "sqlite:///./lesson_6_FastAPI_DB/hw_6/instance/hw_6.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
app = FastAPI()


# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = users.insert().values(firstname=f'firstname{i}',
#                                       lastname=f'lastname{i}',
#                                       email=f'mail{i}@mail.ru',
#                                       password=f'pass{i}')
#         await database.execute(query)
#     return {'message': f'{count} fake users create'}


# @app.get('/fake_product/{count}')
# async def create_note(count: int):
#     for i in range(count):
#         query = products.insert().values(title=f'product{i}',
#                                          description=f'description{i}',
#                                          price=random.randint(1, 1000) * i)
#         await database.execute(query)
#     return {'message': f'{count} fake products create'}


@app.get('/')
async def main():
    return {'message': 'Database created'}


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.columns.id == user_id)
    return await database.fetch_one(query)


@app.get('/users/', response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.post('/users/', response_model=User)
async def create_user(user: User):
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.dict(), 'id': last_record_id}


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserId):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


@app.get('/products/', response_model=List[Product])
async def read_products():
    query = products.select()
    return await database.fetch_all(query)


@app.get('/products/{product_id}', response_model=Product)
async def read_product(product_id: int):
    query = products.select().where(products.columns.id == product_id)
    return await database.fetch_one(query)


@app.post('/products/', response_model=Product)
async def add_product(product: Product):
    query = products.insert().values(**product.dict())
    last_record_id = await database.execute(query)
    return {**product.dict(), 'id': last_record_id}


@app.put('/products/{product_id}', response_model=Product)
async def change_product(product_id: int, new_product: ProductId):
    query = products.update().where(products.c.id == product_id).values(new_product)
    await database.execute(query)
    return {**new_product.dict(), 'id': product_id}


@app.delete('/products/{product_id}', response_model=Product)
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database.execute(query)
    return {'message': 'Product deleted'}


@app.get('/orders/', response_model=List[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)


@app.get('/orders/{order_id}', response_model=Order)
async def read_order(order_id):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)


@app.post('/orders/', response_model=Order)
async def add_order(user_id, product_id, order: Order):
    pass
