# Создать API для получения списка фильмов по жанру.
# Приложение должно иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import logging
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Добро пожаловать в нашу фильмотеку!</h1>"


class Movie(BaseModel):
    id: int
    title: str
    genre: Optional[str] = None
    description: Optional[str] = None
    is_active: bool


movies = []


@app.get('/movies/', response_model=list[Movie])
async def all_movies():
    if len(movies) != 0:
        logger.info('Отработал GET запрос на получение всего списка')
        return movies
    else:
        return HTTPException(status_code=404, detail='Movies not found')


@app.get('/movie/{movie_id/', response_model=Movie)
async def read_movie(movie_id: int):
    for _ in movies:
        if _.id == movie_id:
            logger.info('Отработал GET запрос на получение элемента по ID')
            return _
    return HTTPException(status_code=404, detail='Movie not found')


@app.get('/movie/{movie.genre}/', response_model=list[Movie])
async def sort_genre(movie_genre: str):
    list_genre = []
    for _ in movies:
        if _.genre == movie_genre:
            list_genre.append(_)
    logger.info('Отработал GET запрос на получение элементов по жанру')
    if len(list_genre) != 0:
        return list_genre
    else:
        return HTTPException(status_code=404, detail='Movies not found')


@app.post('/movie/', response_model=Movie)
async def add_movie(movie: Movie):
    movies.append(movie)
    logger.info('Отработал POST запрос добавления элемента')
    return movie


@app.put('/movie/{movie_id}', response_model=Movie)
async def change_movie(movie_id: int, movie: Movie):
    for i, _ in enumerate(movies):
        if _.id == movie_id:
            movies[i] = _
            logger.info('Отработал PUT запрос')
            return _
    return HTTPException(status_code=404, detail='Movie not found')


@app.delete('/movie/{movie_id}', response_model=Movie)
async def delete_movie(movie_id: int):
    for _ in movies:
        if _.id == movie_id:
            _.is_active = False
            logger.info('Отработал DELETE запрос')
            return _
    return HTTPException(status_code=404, detail='Movie not found')
