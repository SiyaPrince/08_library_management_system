from book_operations.view_book import view_books

def select_book(books):
    if not books:
        print("Can't select in empty collection")
        return

    view_books(books)

    selection = input("Select book you want: ").strip()

    if selection.isdigit():
        print("Selection not a digit")
        return

    selection = int(selection)

    if selection < 1 or selection > len(books):
        print("\nInvalid selection. Please enter selection.")
        return

    index = selection - 1

    return books[index]


    

def select_member(members):
    return members[0] if members else None

def select_loan(loans):
    return loans[0] if loans else None


# Check collection isn't empty
# Display numbered records
# Ask user for a selection
# Validate numeric input
# Validate range
# Convert selection to index
# Return selected dictionary