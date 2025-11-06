from fastapi import FastAPI, HTTPException

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
