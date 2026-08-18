from support_operations.displayers import display_book
from support_operations.validators import validate_author_name, validate_book_title, validate_genre
from support_operations.generate_id import generate_next_id


def get_valid_title():
    while True:
        title = input("Enter the name of book: ").strip()
        if validate_book_title(title):
            return title
        print("Title cannot be empty.")


def get_valid_author():
    while True:
        author = input("Enter the name of the author: ").strip()
        if validate_author_name(author):
            return author
        print("Author cannot be empty.")


def get_valid_genre():
    while True:
        genre = input("Enter the genre: ").strip()
        if validate_genre(genre):
            return genre
        print("Genre cannot be empty.")


def book_exists(books: list[dict], title: str, author: str) -> bool:
    """Return True if the same title by the same author already exists."""
    normalized_title = title.strip().lower()
    normalized_author = author.strip().lower()

    for book in books:
        if (
            book["title"].strip().lower() == normalized_title
            and book["author"].strip().lower() == normalized_author
        ):
            return True
    return False


def add_book(books):
    title = get_valid_title()
    author = get_valid_author()
    genre = get_valid_genre()

    if book_exists(books, title, author):
        print("Book already exists.")
        return

    book = {
        "id": generate_next_id(books),
        "title": title,
        "author": author,
        "genre": genre,
        "status": "Available",
    }

    books.append(book)
    print(f"\nThe book {book['title']} by {book['author']} has been added successfully!")
    display_book(book)
