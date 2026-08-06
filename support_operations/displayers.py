def display_book(book):
    print("=" * 45)
    print("\nBook Details:")
    print(f"Book ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Genre: {book['genre']}")
    print(f"\nStatus: {book['status']}")
    print("=" * 45)

def display_member(member):
    print("=" * 45)
    print("\nMember Details:")
    print(f"Member ID: {member['id']}")
    print(f"Name: {member['name']}")
    print(f"Email: {member['email']}")
    print(f"\nStatus: {member['status']}")
    print("=" * 45)

def display_loan(loan, books, members):
    print("=" * 45)
    print("\nLoan Details:")
    print(f"Loan ID: {loan['id']}")
    print(f"Book: {books[loan['book_id']]['title']}")
    print(f"Member: {members[loan['member_id']]['name']}")
    print(f"Due Date: {loan['due_date']}")
    print(f"\nStatus: {loan['status']}")
    print("=" * 45)

def display_menu():
    print("=" * 45)
    print("\nLibrary Management System Menu:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")

    print("6. Add Member")
    print("7. View Members")

    print("8. View Loans")

    print("9. Display Summary")
    print("10. Exit")
    print("=" * 45)

def display_welcome_message():
    print("=" * 45)
    print("\nWelcome to the Library Management System!")
    print("=" * 45)