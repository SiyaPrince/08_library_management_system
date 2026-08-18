from support_operations.displayers import display_welcome_message, display_menu
from book_operations.add_book import add_book
from book_operations.view_book import view_books
from book_operations.search_books import search_books
from loan_operations.borrow_book import borrow_book
from loan_operations.return_book import return_book
from loan_operations.view_loans import view_active_loans
from report_operations.display_summary import display_summary
from member_operations.add_member import add_member
from member_operations.view_members import view_members


def run_library_system():
    books = []
    members = []
    loans = []

    display_welcome_message()

    while True:
        display_menu()
        operation_choice = input("\nPlease choose operation: ").strip()

        if operation_choice == "1":
            add_book(books)
        elif operation_choice == "2":
            search_books(books)
        elif operation_choice == "3":
            borrow_book(books, members, loans)
        elif operation_choice == "4":
            return_book(books, members, loans)
        elif operation_choice == "5":
            view_books(books)
        elif operation_choice == "6":
            add_member(members)
        elif operation_choice == "7":
            view_members(members)
        elif operation_choice == "8":
            view_active_loans(loans, books, members)
        elif operation_choice == "9":
            display_summary(books, members, loans)
        elif operation_choice == "10":
            print("\nExiting the Library Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
