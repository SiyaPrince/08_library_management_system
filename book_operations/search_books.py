from book_operations.view_book import view_books

def search_books(books: list[dict]) -> None:
    if not books:
        print("No books found.")
        return

    search_term = input(
        "Enter the title, author name or genre to search for: "
    ).strip().lower()

    if not search_term:
        print("Search value cannot be empty.")
        return

    found_books = []
    for book in books:
        searchable_values = (
            book["title"].lower(),
            book["author"].lower(),
            book["genre"].lower(),
        )
        if any(search_term in value for value in searchable_values):
            found_books.append(book)

    if not found_books:
        print("book not found.")
        return

    print(f"Found {len(found_books)} matching book(s).")
    view_books(found_books)