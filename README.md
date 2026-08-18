# Library Management System

A command-line Library Management System built with Python that manages books, library members, and book loans.

This project focuses on modelling relationships between different entities, enforcing business rules, managing state changes, and organizing a larger Python application using modules and packages.

## Features

The application allows a user to:

* Add books to the library catalogue
* View all books
* Search for books by title, author, or genre
* Register library members
* View registered members
* Search for members
* Borrow available books
* Return borrowed books
* View active loans
* Display a library summary
* Prevent unavailable books from being borrowed
* Prevent inactive members from borrowing books
* Validate user input
* Generate unique IDs for books, members, and loans

## Data Structure

The application manages three primary entities: **books, members, and loans**.

### Book

Each book is represented by a dictionary:

```python
book = {
    "id": 1,
    "title": "Things Fall Apart",
    "author": "Chinua Achebe",
    "genre": "Fiction",
    "status": "Available"
}
``

Books are stored in a collection:

```python
books = []
```

### Member

Each member is represented by a dictionary:

```python
member = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "status": "Active"
}
```

Members are stored in:

```python
members = []
```

### Loan

Loans represent the relationship between a member and a borrowed book.

```python
loan = {
    "id": 1,
    "book_id": 1,
    "member_id": 1,
    "borrow_date": "2026-08-18",
    "due_date": "2026-09-01",
    "status": "Active"
}
```

Instead of duplicating book and member information, loans reference those entities through their unique IDs.

## Borrowing Workflow

Before a book can be borrowed, the application verifies that:

1. Books and members exist.
2. A valid member has been selected.
3. The selected member is active.
4. A valid book has been selected.
5. The selected book is available.
6. The member does not already have an active loan for the same book.
7. The supplied due date is valid.

Once the checks succeed, a loan is created and the book's status changes from:

```text
Available → Borrowed
```

This ensures that a book cannot have multiple active borrowers at the same time.

## Returning Books

When a book is returned, the application finds the corresponding active loan and updates both related records:

```text
Loan:
Active → Returned

Book:
Borrowed → Available
```

This keeps the state of the book and its loan synchronized.

## Project Structure

```text
library_management_system/
│
├── main.py
├── run_library_system.py
│
├── book_operations/
│   ├── __init__.py
│   ├── add_book.py
│   ├── search_books.py
│   └── view_book.py
│
├── member_operations/
│   ├── __init__.py
│   ├── add_member.py
│   ├── search_members.py
│   └── view_members.py
│
├── loan_operations/
│   ├── __init__.py
│   ├── borrow_book.py
│   ├── return_book.py
│   └── view_loans.py
│
├── report_operations/
│   ├── __init__.py
│   └── display_summary.py
│
└── support_operations/
    ├── __init__.py
    ├── displayers.py
    ├── generate_id.py
    ├── selectors.py
    └── validators.py
```

The application is separated into packages based on responsibility:

* **`book_operations`** — book-related functionality
* **`member_operations`** — member-related functionality
* **`loan_operations`** — borrowing and returning functionality
* **`report_operations`** — library reporting
* **`support_operations`** — reusable validation, display, ID generation, and selection functionality

The `__init__.py` files identify these directories as Python packages.

## Running the Application

Ensure Python 3 is installed.

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd library_management_system
```

Run:

```bash
python main.py
```

The application will display an interactive menu from which library operations can be selected.

## Concepts Applied

This project applies several Python and software-development concepts:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Input validation
* Exception handling
* List comprehensions
* Modules
* Packages
* Imports
* Unique identifiers
* Entity relationships
* Collection filtering
* Searching
* Aggregation
* State management
* Separation of concerns
* Modular programming
* Guard clauses
* Reusable helper functions

## Key Engineering Concepts

### Entity Relationships

Unlike simpler CRUD applications where records exist independently, this application contains related entities.

A loan connects:

```text
Member
   ↓
 Loan
   ↑
 Book
```

The relationship is maintained using `member_id` and `book_id`.

### State Management

The application must keep related state synchronized.

Borrowing changes a book to `Borrowed`, while returning it changes the book back to `Available`.

The loan itself also has a lifecycle:

```text
Active → Returned
```

### Business Rules

The application distinguishes basic input validation from business rules.

For example, `"2026-09-01"` being a valid date is a validation concern.

A borrowed book not being allowed to be borrowed again is a **business rule**.

### Separation of Concerns

Functionality is divided into dedicated packages and modules instead of placing the entire application inside a single Python file.

This improves readability, maintainability, and reusability.

## Current Limitations

This version intentionally remains a command-line, in-memory application.

As a result:

* Data is lost when the application closes.
* There is no database.
* There is no user authentication.
* Books represent individual records rather than multiple physical copies of the same title.
* There is no reservation system.
* There are no overdue penalties.
* There is no graphical or web interface.

## Future Improvements

The Library Management System could be expanded considerably.

Potential improvements include:

* Persistent storage using JSON or CSV
* SQLite or another relational database
* Multiple physical copies of the same book
* Member borrowing limits
* Member suspension
* Overdue-loan detection
* Late-return penalties
* Book reservations and waiting lists
* Complete borrowing history
* Book and member editing
* Safe book and member deletion
* More detailed reporting and statistics
* Most frequently borrowed books
* Most active members
* Authentication and authorization
* Automated tests
* REST API
* Web-based user interface

A database-backed version would be particularly valuable because the relationships currently represented through IDs naturally map to relational database concepts such as **primary keys and foreign keys**.

## What This Project Demonstrates

The Library Management System represents a progression beyond basic standalone CRUD applications.

It demonstrates the ability to model multiple related entities, establish relationships through identifiers, enforce business rules across collections, synchronize state changes, aggregate application data, and organize a Python project into reusable packages and modules.

These concepts provide a foundation for larger systems that use databases, APIs, and persistent storage.

## Technologies

* Python 3
* Python Standard Library
* Command-Line Interface (CLI)

## License

This project is intended for educational and portfolio purposes.
