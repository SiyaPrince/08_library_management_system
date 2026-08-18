from support_operations.displayers import display_book, display_member, display_loan
from support_operations.selectors import select_loan


def _find_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def return_book(books, members, loans):
    selected_loan = select_loan(loans, books, members)
    if selected_loan is None:
        return

    selected_book = _find_by_id(books, selected_loan["book_id"])
    selected_member = _find_by_id(members, selected_loan["member_id"])

    if selected_book is None:
        print("Book associated with this loan could not be found.")
        return

    print("\nSelected loan:")
    display_loan(selected_loan, books, members)
    display_book(selected_book)
    if selected_member is not None:
        display_member(selected_member)

    confirmation = input("Confirm return? (Y/N): ").strip().lower()
    if confirmation not in ("y", "yes"):
        print("Return cancelled.")
        return

    selected_loan["status"] = "Returned"
    selected_book["status"] = "Available"

    print(f"The book '{selected_book['title']}' has been successfully returned.")
