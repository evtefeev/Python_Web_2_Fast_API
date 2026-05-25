@app.get("/books/{isbn}/{year}")
async def get_book(
    isbn: str = Path(..., title="The ISBN of the book"),
    year: int = Path(..., ge=1900, le=2024, title="The year of the book publication")
):
    book_data = fetch_book_data(isbn, year)
    if book_data:
        return book_data
    return {"error": "Book not found"}


def fetch_book_data(isbn, year):
    sample_books = [
        {"isbn": "1234567890", "year": 1995, "title": "Book One", "author": "Author A"},
        {"isbn": "0987654321", "year": 2005, "title": "Book Two", "author": "Author B"},
    ]
    book = next((b for b in sample_books if b["isbn"] == isbn and b["year"] == year), None)
    return book