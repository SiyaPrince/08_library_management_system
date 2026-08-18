import re
from datetime import date


def validate_email(email):
    regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,63}"
    return re.fullmatch(regex, email) is not None


def validate_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10


def validate_date(date_value):
    try:
        date.fromisoformat(date_value)
    except ValueError:
        return False
    return True


def validate_book_title(title):
    return bool(title.strip())


def validate_member_name(name):
    return bool(name.strip())


def validate_author_name(name):
    return bool(name.strip())


def validate_genre(genre):
    return bool(genre.strip())


def validate_due_date(due_date):
    return validate_date(due_date)
