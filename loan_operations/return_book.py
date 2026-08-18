from support_operations.displayers import display_book, display_member, display_loan
from support_operations.selectors import select_loan


def return_book(books, members, loans):

    # Check if there are active loans
    active_loans = [
        loan for loan in loans
        if loan["status"] == "Active"
    ]

    # If none -> return
    if not active_loans:
        print("There are no active loans.")
        return

    # Select an active loan
    selected_loan = select_loan(active_loans, books, members)

    # If cancelled / invalid -> return
    if selected_loan is None:
        return

    # Find the book whose id matches selected_loan["book_id"]
    selected_book = None

    for book in books:
        if book["id"] == selected_loan["book_id"]:
            selected_book = book
            break

    # If book cannot be found -> return
    if selected_book is None:
        print("Book associated with this loan could not be found.")
        return

    # Optionally find the member whose id matches selected_loan["member_id"]
    selected_member = None

    for member in members:
        if member["id"] == selected_loan["member_id"]:
            selected_member = member
            break

    # Display loan details
    display_loan(selected_loan, books, members)
    display_book(selected_book)

    if selected_member is not None:
        display_member(selected_member)

    # Confirm return
    confirmation = input("Confirm return? (Y/N): ").strip().upper()

    if confirmation != "Y":
        print("Return cancelled.")
        return

    # Set loan status to Returned
    selected_loan["status"] = "Returned"

    # Set book status to Available
    selected_book["status"] = "Available"

    # Display success
    print(
        f"The book '{selected_book['title']}' "
        f"has been successfully returned."
    )
