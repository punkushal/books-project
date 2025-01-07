from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'first title','category':'science'},
    {'title': 'second title','category':'tech'},
    {'title': 'third title','category':'science'},
    {'title': 'fourth title','category':'history'},
    {'title': 'fivth title','category':'education'},
]

@app.get('/books')
def read_all_books():
    return BOOKS