from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

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
    id: int = Field(description='ID is optional which is automatically assigned behind the scene', default=None)
    title: str= Field(min_length=5)
    director: str = Field(min_length=10 , max_length=20)
    description: str = Field(min_length=1, max_length=100)
    ratings: int = Field(gt=-1, lt=10)
   
    model_config = {
        'json_schema_extra':{
            'example':{
                'title':'new title of a movie',
                'director': 'new director',
                'description': 'a new description',
                'ratings':6
            }
        }
    }


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


# fetch movie by id
@app.get('/movies/{movie_id}')
def fetch_movie(movie_id : int  = Path(gt=0)):
    for movie in MOVIES:
        if movie.id == movie_id:
            return movie
    
# fetch movies list by rating
# query parameter as /movies followed by another /
@app.get('/movies/')
def fetch_movies_by_rating(rating : int = Path(gt=0 , lt=10)):
    movies_to_return = []
    for movie in MOVIES:
        if movie.ratings == rating:
            movies_to_return.append(movie)
    return movies_to_return


# To create new movie object
@app.post('/create_movie')
def create_movie(movie_request : MovieRequest):
    # ** expands the dictionary created by model_dump() to the constructor requirement
    new_movie = Movie(**movie_request.model_dump())
    MOVIES.append(find_movie_id(new_movie))
    return "successfully added new movie object"


def find_movie_id(movie : Movie):
    movie.id = 0 if len(MOVIES)==0 else MOVIES[-1].id + 1
    return movie

# UPDATE EXISTING MOVIE
@app.put('/movies/update_movie')
def update_movie(movie : MovieRequest):
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie.id:
            MOVIES[i] = movie
    return "successfully updated existing book details"

# DELETE MOVIE BY PASSING BOOK ID
@app.delete('/movies/{movie_id}')
def delete_movie(movie_id : int = Path(gt=0)):
    for i in range(len(MOVIES)):
        if MOVIES[i].id == movie_id:
            MOVIES.pop(i)
            break
    