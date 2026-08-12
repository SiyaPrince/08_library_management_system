from support_operations.displayers import display_book


def get_valid_title():return

def get_valid_author():return

def get_valid_genre():return

def add_book(books):
   
    # Ask for input

    title = get_valid_title()
    author = get_valid_author()
    genre = get_valid_genre()

    # Add to dictionary
    book = {
        "book_id": id,
        "title": "title",
        "author": "author",
        "genre": "genre",
        "status": "Available"
    }

    books.append(book)

    print(f"\nThe book {book['title']} by {book['author']} has been added successfully!!")

    display_book(book)