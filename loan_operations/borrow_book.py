from support_operations.displayers import display_book, display_member, display_loan
from book_operations.add_book import book_exists
from member_operations.add_member import member_exists
from support_operations.selectors import select_member, select_book
from support_operations.generate_id import generate_next_id
from support_operations.validators import validate_due_date


def get_due_date():
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()

        if validate_due_date(due_date):
            return due_date

        print("Please re-enter the due date.")


def borrow_book(books, members, loans):

    # Check books exist
    if not books:
        print("No books exist.")
        return

    # Check members exist
    if not members:
        print("No members exist.")
        return

    # Select member
    member = select_member(members)

    # Cancelled / invalid selection
    if member is None:
        return

    display_member(member)

    # Check member is Active
    if member["status"] != "Active":
        print("Member is not Active.")
        return

    # Select book
    book = select_book(books)

    # Cancelled / invalid selection
    if book is None:
        return

    display_book(book)

    # Check book is Available
    if book["status"] != "Available":
        print("Book is not Available.")
        return

    # Check whether there is already an Active loan
    # for this same member + same book
    for loan in loans:
        if (
            loan["member_id"] == member["id"]
            and loan["book_id"] == book["id"]
            and loan["status"] == "Active"
        ):
            print("This member already has an Active loan for this book.")
            return

    # Ask for due date
    due_date = get_due_date()

    # Generate loan ID
    loan_id = generate_next_id(loans)

    # Create loan
    loan = {
        "id": loan_id,
        "book_id": book["id"],
        "member_id": member["id"],
        "due_date": due_date,
        "status": "Active"
    }

    # Append loan
    loans.append(loan)

    # Set book status to Borrowed
    book["status"] = "Borrowed"

    # Display success
    print(
        f"The book '{book['title']}' has been successfully "
        f"borrowed by member '{member['name']}'."
    )
