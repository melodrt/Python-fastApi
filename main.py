from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
app.title = "Mi primera API con FastAPI"
app.version = "1.0.0"

class Movie(BaseModel):
    id: int
    title:str
    overview:str
    year:int
    rating:float
    category:str

class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int
    rating:float
    category:str
    
movies = [
    {
        "id": 1,
        "title": "El Padrino",
        "overview": "La historia de la familia Corleone.",
        "year": 1972,
        "rating": 9.2,
        "category": "Drama"
    },
    {
        "id": 2,    
        "title": "The Dark Knight",
        "overview": "Batman enfrenta al Joker en Gotham City.",
        "year": 2008,
        "rating": 9.0,
        "category": "Action"
    },
    {
    "id": 3,
    "title": "Nueva Película",
    "overview": "Descripción de la nueva película",
    "year": 2023,
    "rating": 8.5,
    "category": "Action"
    }
]


#METODO GET
@app.get("/home", tags=["Home"])
def home():
    return "Hola mundo"

@app.get("/movies", tags=["Movies"])
def get_movies() -> List[Movie]:
    return movies

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get('/movies/', tags=["Movies"])
def get_movie_by_category(category: str) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO POST
@app.post('/movies', tags=["Movies"])
def create_movie(movie: Movie) -> List[Movie]:
    movies.append(movie.model_dump())
    return movies

#METODO PUT
@app.put('/movies/{id}', tags=["Movies"])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO DELETE
@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movies
    raise HTTPException(status_code=404, detail="Movie not found")

