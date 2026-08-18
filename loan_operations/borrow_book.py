from datetime import date

from support_operations.displayers import display_book, display_member
from support_operations.selectors import select_member, select_book
from support_operations.generate_id import generate_next_id
from support_operations.validators import validate_due_date


def get_due_date():
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if validate_due_date(due_date):
            return due_date
        print("Invalid due date. Please use a real date in YYYY-MM-DD format.")


def borrow_book(books, members, loans):
    if not books:
        print("No books exist.")
        return

    if not members:
        print("No members exist.")
        return

    member = select_member(members)
    if member is None:
        return

    display_member(member)
    if member["status"] != "Active":
        print("Member is not active.")
        return

    book = select_book(books)
    if book is None:
        return

    display_book(book)
    if book["status"] != "Available":
        print("Book is not available.")
        return

    for loan in loans:
        if (
            loan["member_id"] == member["id"]
            and loan["book_id"] == book["id"]
            and loan["status"] == "Active"
        ):
            print("This member already has an active loan for this book.")
            return

    due_date = get_due_date()
    borrow_date = date.today().isoformat()

    if due_date < borrow_date:
        print("Due date cannot be earlier than the borrow date.")
        return

    loan = {
        "id": generate_next_id(loans),
        "book_id": book["id"],
        "member_id": member["id"],
        "borrow_date": borrow_date,
        "due_date": due_date,
        "status": "Active",
    }

    loans.append(loan)
    book["status"] = "Borrowed"

    print(
        f"The book '{book['title']}' has been successfully "
        f"borrowed by member '{member['name']}'."
    )
