def display_book(book):
    print(f"Book ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Genre: {book['genre']}")
    print(f"Status: {book['status']}")

def display_member(member):
    print(f"Member ID: {member['id']}")
    print(f"Name: {member['name']}")
    print(f"Email: {member['email']}")
    print(f"Status: {member['status']}")

def display_loan(loan, books, members):
    print(f"Loan ID: {loan['id']}")
    print(f"Book: {books[loan['book_id']]['title']}")
    print(f"Member: {members[loan['member_id']]['name']}")
    print(f"Due Date: {loan['due_date']}")
    print(f"Status: {loan['status']}")