
#define a function

#

# def view_tasks(user_data):
#     print(f"{user_data['name']} is viewing tasks")

# def submit_tasks(user_data):
#     if user_data == "manager":
#         print(f"{user_data['name']} is submitting tasks")
#     else:
#         print("the manager no need submit tasks")

# def assign_tasks(user_data):
#     if user_data == "manager":
#         print(f"{user_data['name']} is assign tasks")
#     else:
#         print(" team members can't assign  the tasks")


#

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic Model
class Book(BaseModel):
    book_id: int
    name: str
    type: str
    description: str
    author: str



class BookManager:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        return {
            "message": "Book added successfully",
            "book": book
        }

    def get_books(self):
        return self.books

    def update_book(self, book_id: int, updated_book: Book):

        for index, book in enumerate(self.books):

            if book.book_id == book_id:
                self.books[index] = updated_book

                return {
                    "message": "Book updated successfully",
                    "book": updated_book
                }

        return {"message": "Book not found"}

    def delete_book(self, book_id: int):

        for index, book in enumerate(self.books):

            if book.book_id == book_id:
                deleted_book = self.books.pop(index)

                return {
                    "message": "Book deleted successfully",
                    "book": deleted_book
                }

        return {"message": "Book not found"}



book_manager = BookManager()


# CREATE
@app.post("/books")
def add_book(book: Book):
    return book_manager.add_book(book)


# READ
@app.get("/books")
def get_books():
    return book_manager.get_books()


# UPDATE
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    return book_manager.update_book(book_id, updated_book)


# DELETE
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    return book_manager.delete_book(book_id)









#data collection
# users = ["name":"nani","role":"manager"]

# #function to be called

# login(user_data)
# view_tasks(user_data)
# submit_tasks(user_data)
# assign_tasks(user_data) 