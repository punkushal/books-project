from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Movie:
    id: int
    title: str
    director: str
    description: str
    ratings: int

    def __init__(self, id: int, title: str, director: str, description: str, ratings: int):
        self.id = id
        self.title = title
        self.director = director
        self.description = description
        self.ratings = ratings

class MovieRequest(BaseModel):
    id: int
    title: str
    director: str
    description: str
    ratings: int


MOVIES = [
        Movie(id=1, title='Dark Knight', director="Crishtophor Nolan", description="Batman movie",ratings=8),
        Movie(id=2, title='Parasite', director="Bong Joon-ho", description="A poor family schemes to infiltrate the lives of a wealthy family",ratings=8.6),
        Movie(id=3, title='The Intouchables', director="Oliver Nakache & Eric Tolendano", description="Friendship",ratings=8.5),
        Movie(id=4, title='City of God', director="Fernando Meirelles & Katia Lund", description="Depicting the rise of drug gangs",ratings=8.6),
        Movie(id=5, title='Tare Zameen Par', director="Aamir Khan", description="Teacher helps his student to realize his potential",ratings=8.4),
]

# fetching all movies
@app.get('/movies')
def fetch_all_movies():
    return MOVIES


# To create new movie object
@app.post('/create_movie')
def create_movie(movie_request : MovieRequest):
    # ** expands the dictionary created by model_dump() to the constructor requirement
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(new_movie)
    return "successfully added new movie object"
