from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Sample data - a list of books
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "genre": "Romance"},
    {"id": 5, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction"}
]

# TODO: Create a Pydantic model for Book data validation
class Book(BaseModel):
    pass  # Add fields here

# TODO: Implement GET endpoint at root "/"
# Should return a welcome message

# TODO: Implement GET endpoint at "/books"
# Should return all books

# TODO: Implement GET endpoint at "/books/{book_id}"
# Should return a specific book or 404 if not found

# TODO: Implement POST endpoint at "/books"
# Should create a new book and add it to the collection

# TODO: Implement PUT endpoint at "/books/{book_id}"
# Should update an existing book or return 404 if not found

# TODO: Implement DELETE endpoint at "/books/{book_id}"
# Should delete a book or return 404 if not found

# To run this application, use the command:
# uvicorn starter-code:app --reload
