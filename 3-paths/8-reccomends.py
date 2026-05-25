sample_books = [
    {"title": "1984", "genre": "dystopia", "rating": 4.6},
    {"title": "To Kill a Mockingbird", "genre": "classic", "rating": 4.8},
    {"title": "Brave New World", "genre": "dystopia", "rating": 3.9}
]
@app.get("/book-recommendations/")
async def get_book_recommendations(
    genre: str,
    min_rating: float = Query(4.0, gt=0, le=5)
):
    recommendations = fetch_book_recommendations(genre, min_rating)
    return {"books": recommendations}




def fetch_book_recommendations(genre, min_rating):
    sample_books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "novel", "rating": 4.3},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "novel", "rating": 4.8},
        {"title": "1984", "author": "George Orwell", "genre": "dystopian", "rating": 4.2},
    ]
    filtered_books = [book for book in sample_books if book["genre"] == genre and book["rating"] >= min_rating]
    return filtered_books
