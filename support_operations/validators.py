import re

def validate_email(email):
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"

    if not re.fullmatch(regex, email):
        print("\nInvalid email. Please enter valid email, with '@' and '.'")
        return False
    return True

def validate_phone_number(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("\nInvalid phone number. Please enter a 10-digit number.")
        return False
    return True

def validate_date(date):
    try:
        year, month, day = map(int, date.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except ValueError:
        print("\nInvalid date format. Please use YYYY-MM-DD.")
        return False
    return True

def validate_book_title(title):
    if not title:
        print("\nBook title cannot be empty.")
        return False
    return True

def validate_member_name(name):
    if not name:
        print("\nMember name cannot be empty.")
        return False
    return True

def validate_author_name(name):
    if not name:
        print("\nAuthor name cannot be empty.")
        return False
    return True