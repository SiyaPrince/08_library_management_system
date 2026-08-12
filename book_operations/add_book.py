from support_operations.displayers import display_book
from support_operations.validators import validate_author_name, validate_book_title, validate_genre

def get_valid_title():
     while True:
             name = input("Enter the name of book: ").strip()
             if validate_book_title(name):
                 return name
             print("Title cannot be empty.")

def get_valid_author():
    while True:
            name = input("Enter the name of the author: ").strip()
            if validate_author_name(name):
                return name
            print("Author cannot be empty.")

def get_valid_genre():
     while True:
             name = input("Enter the genre: ").strip()
             if validate_genre(name):
                 return name
             print("Genre cannot be empty.")


def book_exists(books: list[dict], title : str, author: str, genre: str) -> bool:
    """Return True if a phone number or supplied email already exists."""
    normalized_title = title.lower()
    normalized_author = author.lower()
    normalized_genre = genre.lower()
    for contact in books:
        if normalized_title and normalized_author and normalized_genre:
            print("Book already exists.")
            return True
    return False

def add_book(books):
   
    # Ask for input

    title = get_valid_title()
    author = get_valid_author()
    genre = get_valid_genre()

    if book_exists(books, title,author, genre):
         return

    # Add to dictionary
    book = {
        "book_id": id,
        "title": title,
        "author": author,
        "genre": genre,
        "status": "Available"
    }

    books.append(book)

    print(f"\nThe book {book['title']} by {book['author']} has been added successfully!!")

    display_book(book)