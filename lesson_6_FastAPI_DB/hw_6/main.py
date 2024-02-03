# Напишите API для управления списком задач. Для этого создайте модель Task
# со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)

# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.

import random
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

DATABASE_URL = "sqlite:///./lesson_6_FastAPI_DB/hw_6/instance/hw_6.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(32)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("done", sqlalchemy.Boolean())
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
app = FastAPI()


class Task(BaseModel):
    title: str = Field(max_length=32)
    description: str = Field(max_length=512)
    done: bool = Field()


class TaskId(Task):
    id: int


@app.get('/')
async def hello():
    return {'Сообщение': 'Почти ToDo!'}


# @app.get("/fake_tasks/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         query = tasks.insert().values(title=f'task_{i}',
#                                       description=f'description_{i}',
#                                       done=random.choice([True, False]))
#         await database.execute(query)
#     return {'message': f'{count} fake tasks create'}


@app.post('/tasks/', response_model=TaskId)
async def create_task(task: Task):
    query = tasks.insert().values(**task.model_dump())
    last_record_id = await database.execute(query)
    return {**task.model_dump(), 'id': last_record_id}


@app.get('/tasks/', response_model=List[TaskId])
async def read_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@app.get("/tasks/{task_id}", response_model=TaskId)
async def read_task(task_id: int):
    query = tasks.select().where(tasks.columns.id == task_id)
    print(query)
    return await database.fetch_one(query)


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, new_task: TaskId):
    query = tasks.update().where(tasks.c.id == task_id).values(**new_task.dict())
    await database.execute(query)
    return {**new_task.dict(), "id": task_id}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {'message': 'task deleted'}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
