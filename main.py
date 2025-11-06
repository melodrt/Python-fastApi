from fastapi import FastAPI

app = FastAPI()
app.title = "Mi primera API con FastAPI"
app.version = "1.0.0"

movie = [
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
    return movie