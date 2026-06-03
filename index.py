from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory database
books = []

# Pydantic Model
class Book(BaseModel):
    book_id: int
    name: str
    type: str
    description: str
    author: str

# CREATE Operation
@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {
        "message": "Book added successfully",
        "book": book
    }




# READ Operation
@app.get("/books")
def get_books():
    return books


# UPDATE Operation
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):

        if book.book_id == book_id:
            books[index] = updated_book

            return {
                "message": "Book updated successfully",
                "book": updated_book
            }

    return {"message": "Book not found"}


# DELETE Operation
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for index, book in enumerate(books):

        if book.book_id == book_id:
            deleted_book = books.pop(index)

            return {
                "message": "Book deleted successfully",
                "book": deleted_book
            }

    return {"message": "Book not found"}