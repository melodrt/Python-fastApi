from fastapi import FastAPI, HTTPException, Body

app = FastAPI()
app.title = "Mi primera API con FastAPI"
app.version = "1.0.0"

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
    }
]

#METODO GET
@app.get("/home", tags=["Home"])
def home():
    return "Hola mundo"

@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=["Movies"])
def get_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            return movie
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

@app.get('/movies/', tags=["Movies"])
def get_movi_by_category(category: str):
    for movie in movies:
        if movie['category'] == category:
            return movie
    # Si no encontramos la película, devolvemos 404
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO POST
@app.post('/movies', tags=["Movies"])
def create_movie(
    id: int = Body(), 
    title: str = Body(), 
    overview: str = Body(), 
    year: int =Body(), 
    rating: float = Body(), 
    category: str = Body()
    ):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies

#METODO PUT
@app.put('/movies/{id}', tags=["Movies"])
def update_movie(
    id: int,
    title: str = Body(), 
    overview: str = Body(), 
    year: int =Body(), 
    rating: float = Body(), 
    category: str = Body()
):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category
            return movies
    raise HTTPException(status_code=404, detail="Movie not found")

#METODO DELETE
@app.delete('/movies/{id}', tags=["Movies"])
def delete_movie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            return movies
    raise HTTPException(status_code=404, detail="Movie not found")

