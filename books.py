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

#getting book with title name which will be path parameter
@app.get('/books/{book_title}')
def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.get('/books/{dynamic_param}')
def read_all_books(dynamic_param):
    return {'dynamic':dynamic_param}