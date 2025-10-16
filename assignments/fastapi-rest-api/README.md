# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a functional API with multiple endpoints, request validation, and proper HTTP methods to manage a collection of resources. This assignment will introduce you to web API development, HTTP protocols, and the FastAPI framework.

## 📝 Tasks

### 🛠️ Setup and Basic Endpoints

#### Description
Set up a FastAPI project and create basic GET endpoints to retrieve data. You'll build an API that manages a collection of books with information like title, author, year, and genre.

#### Requirements
Completed program should:

- Install and import FastAPI and uvicorn packages
- Create a FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/books` that returns a list of all books
- Implement a GET endpoint at `/books/{book_id}` that returns a specific book by ID
- Include at least 5 sample books in your initial data collection


### 🛠️ POST and PUT Endpoints

#### Description
Implement endpoints to create new books and update existing ones. You'll learn to handle request bodies and validate incoming data.

#### Requirements
Completed program should:

- Create a Pydantic model to validate book data (title, author, year, genre)
- Implement a POST endpoint at `/books` to add a new book to the collection
- Validate that all required fields are provided in the request body
- Implement a PUT endpoint at `/books/{book_id}` to update an existing book
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Return the created or updated book data in the response


### 🛠️ DELETE Endpoint and Error Handling

#### Description
Complete your API by adding deletion functionality and proper error handling for edge cases.

#### Requirements
Completed program should:

- Implement a DELETE endpoint at `/books/{book_id}` to remove a book from the collection
- Return a 404 status code with an error message when a book is not found
- Return a 400 status code for invalid requests (e.g., invalid book ID format)
- Include automatic API documentation at `/docs` (provided by FastAPI)
- Test all endpoints using the interactive documentation or a tool like curl/Postman
- Include clear success and error messages in all responses
