def _find_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def display_book(book):
    print("=" * 45)
    print("\nBook Details:")
    print(f"Book ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Genre: {book['genre']}")
    print(f"Status: {book['status']}")
    print("=" * 45)


def display_member(member):
    print("=" * 45)
    print("\nMember Details:")
    print(f"Member ID: {member['id']}")
    print(f"Name: {member['name']}")
    print(f"Email: {member['email']}")
    print(f"Status: {member['status']}")
    print("=" * 45)


def display_loan(loan, books, members):
    book = _find_by_id(books, loan["book_id"])
    member = _find_by_id(members, loan["member_id"])

    book_name = book["title"] if book else f"Unknown book (ID {loan['book_id']})"
    member_name = member["name"] if member else f"Unknown member (ID {loan['member_id']})"

    print("=" * 45)
    print("\nLoan Details:")
    print(f"Loan ID: {loan['id']}")
    print(f"Book: {book_name}")
    print(f"Member: {member_name}")
    print(f"Borrow Date: {loan['borrow_date']}")
    print(f"Due Date: {loan['due_date']}")
    print(f"Status: {loan['status']}")
    print("=" * 45)


def display_menu():
    print("=" * 45)
    print("\nLibrary Management System Menu:")
    print("1. Add Book")
    print("2. Search Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. Add Member")
    print("7. View Members")
    print("8. View Active Loans")
    print("9. Display Summary")
    print("10. Exit")
    print("=" * 45)


def display_welcome_message():
    print("=" * 45)
    print("\nWelcome to the Library Management System!")
    print("=" * 45)
