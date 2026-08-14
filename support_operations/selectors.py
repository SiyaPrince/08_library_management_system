from book_operations.view_book import view_books
from member_operations.view_members import view_members
from loan_operations.view_loans import view_active_loans

def select_book(books):
    if not books:
        print("Can't select from an empty collection.")
        return

    view_books(books)

    selection = input("Select book you want: ").strip()

    if not selection.isdigit():
        print("Selection must be a number.")
        return

    selection = int(selection)

    if selection < 1 or selection > len(books):
        print("Invalid selection. Please choose a valid number.")
        return

    index = selection - 1

    return books[index]

def select_member(members):
    if not members:
        print("Can't select from an empty collection.")
        return

    view_members(members)

    selection = input("Select member you want: ").strip()

    if not selection.isdigit():
        print("Selection must be a number.")
        return

    selection = int(selection)

    if selection < 1 or selection > len(members):
        print("Invalid selection. Please choose a valid number.")
        return

    index = selection - 1

    return members[index]

def select_loan(loans, books, members):
    active_loans = []

    for loan in loans:
        if loan["status"] == "Active":
            active_loans.append(loan)

    if not active_loans:
        print("No active loans available.")
        return

    view_active_loans(active_loans, books, members)

    selection = input("Select book loan you want: ").strip()

    if not selection.isdigit():
        print("Selection must be a number.")
        return

    selection = int(selection)

    if selection < 1 or selection > len(active_loans):
        print("Invalid selection. Please choose a valid number.")
        return

    index = selection - 1

    return active_loans[index]