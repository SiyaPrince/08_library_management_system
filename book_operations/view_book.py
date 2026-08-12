from support_operations.displayers import display_book


def view_books(books: list[dict]) -> None:
    if not books:
        print("No books found.")
        return

    print(f"\nBooks: ({len(books)})")
    print("=" * 45)
    for number, book in enumerate(books, start=1):
        display_book(book, number)
