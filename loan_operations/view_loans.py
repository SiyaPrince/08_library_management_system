from support_operations.displayers import display_loan

def view_active_loans(loans: list[dict],
                 books: list[dict],
                 members: list[dict]) -> None:
    if not loans:
        print("No loans found.")
        return

    print(f"\Loans: ({len(loans)})")
    print("=" * 45)

    for number, loan in enumerate(loans, start=1):
        print(f"\nMember {number}")
        display_loan(loan, books, members)