from fastapi import FastAPI, HTTPException, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, ConfigDict
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

class MovieCreate(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            'examples': [
                {
                    'id': 1,
                    'title': 'Mi película',
                    'overview': 'Descripción de la película',
                    'year': 2025,
                    'rating': 5.0,
                    'category': 'Acción'
                }
            ]
        }
    )
    
    id: int
    title:str = Field(min_length=5, max_length=15)
    overview:str = Field(min_length=15, max_length=50)
    year:int = Field(gt=1900, lt=2025)
    rating:float = Field(gt=0, lt=10)
    category:str = Field(min_length=5, max_length=15)

class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int
    rating:float
    category:str
    
movies: List[Movie] = [
    
]

#METODO GET
@app.get("/home", tags=["Home"])
def home():
    return "Hola mundo"

@app.get("/movies", tags=["Movies"])
def get_movies() -> List[Movie]:
    return [movie.model_dump() for movie in movies]

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int) -> Movie:
    for movie in movies:
        if movie['id'] == id:
            return movie.model_dump()
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get('/movies/', tags=["Movies"])
def get_movie_by_category(category: str) -> Movie:
    for movie in movies:
        if movie['category'] == category:
            return movie.model_dump()
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO POST
@app.post('/movies', tags=["Movies"])
def create_movie(movie: MovieCreate) -> List[Movie]:
    movies.append(movie)
    return [movie.model_dump() for movie in movies]

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
            return [movie.model_dump() for movie in movies]
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO DELETE
@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return [movie.model_dump() for movie in movies]
    raise HTTPException(status_code=404, detail="Movie not found")

