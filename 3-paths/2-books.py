from fastapi import FastAPI, HTTPException
from pydantic import Field, BaseModel
import uvicorn


app = FastAPI()

next_id = 4
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]


class Book(BaseModel):
    id: None | int = Field(None)
    title: str = Field(..., description="Book title", min_length=3)
    author: str = Field(..., description="Book author", min_length=3)


@app.get("/books/")
def get_books():
    return {"books": books}


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return {"book": book}
    raise HTTPException(
        status_code=404, detail="Книгу з таким ID не знайдено."
    ) @ app.post("/books/")


@app.post("/books/")
async def create_book(book: dict):
    global next_id
    book['id'] = next_id
    next_id += 1
    books.append(book)
    return {"message": "Нова книга була додана!", "book": book}


if __name__ == "__main__":
    uvicorn.run(app)
