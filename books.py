from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'title': 'first title','category':'science'},
    {'title': 'second title','category':'tech'},
    {'title': 'third title','category':'science'},
    {'title': 'fourth title','category':'history'},
    {'title': 'fivth title','category':'education'},
]

# get request method examples
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

# Example of query parameter
@app.get('/books/')
def read_books_by_category(category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

## POST REQUEST METHOD EXAMPLES
@app.post('/books/create_book')
def create_book(new_book = Body()):
    BOOKS.append(new_book)
    return "one new book is successfully added."

## PUT REQUEST METHOD EXAMPLE
@app.put('/books/update_book')
def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book
    return "selected book by the title is updated successfully"