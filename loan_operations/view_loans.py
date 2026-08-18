from support_operations.displayers import display_loan


def view_active_loans(
    loans: list[dict],
    books: list[dict],
    members: list[dict]
) -> None:

    active_loans = [
        loan for loan in loans
        if loan["status"] == "Active"
    ]

    if not active_loans:
        print("No active loans found.")
        return

    print(f"\nActive Loans: ({len(active_loans)})")
    print("=" * 45)

    for number, loan in enumerate(active_loans, start=1):
        print(f"\nLoan {number}")
        display_loan(loan, books, members)
