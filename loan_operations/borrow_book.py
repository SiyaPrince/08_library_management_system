from support_operations.displayers import display_book, display_member, display_loan
from book_operations.add_book import book_exists, get_valid_title
from member_operations.add_member import member_exists, get_valid_name
from support_operations.selectors import select_member
from support_operations.selectors import select_book
from support_operations.generate_id import generate_next_id
from support_operations.validators import validate_due_date

def get_due_date():

    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()

        # Validate task details
        if validate_due_date(due_date):
            return due_date
        else:
            print("Please re-enter the due date.")

def borrow_book(books, members, loans):

    # Check books exist
    if book_exists(books, title, author, genre):
        return
    
    # Check members exist
    if member_exists(members, name, email):
        return

    # Select member
    member = select_member(members)

    # Confirm member exists
    display_member(member)
    
    # Confirm member is Active
    if member['status'] == 'Active':
           return

    # Select book
    book = select_book(books)

    # Confirm book exists
    display_book(book)
    
    
    # Confirm book is Available
    if book['status'] == 'Available':
               return

    # Check member is not already borrowing that book

    # Prepare loan data

    loan_id = generate_next_id(loans)
    title = get_valid_title()
    member = get_valid_name()
    due_date = get_due_date()

    # Create loan record

    loan = {
        "id" : loan_id,
        "title" : title,
        "member" : member,
        "due_date" : due_date,
        "status" : "Available"
    }

    # Append loan to loans collection
    loans.append(loan)

    # Change book status to Borrowed
    loan["status"] == "Borrowed"

    # Display success
    print(f"The book '{books['title']}' has been successfully borrowed by member '{members['name']}'.")

    return