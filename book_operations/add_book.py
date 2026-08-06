from support_operations.displayers import display_book

def add_book(books):
   
    # Ask for input

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