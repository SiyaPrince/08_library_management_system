from support_operations.displayers import display_member
from support_operations.generate_id import generate_next_id
from support_operations.validators import validate_member_name, validate_email


def get_valid_name():
    while True:
        name = input("Enter the name of the member: ").strip()
        if validate_member_name(name):
            return name
        print("Member name cannot be empty.")


def get_valid_email():
    while True:
        email = input("Enter the email: ").strip()
        if validate_email(email):
            return email
        print("Invalid email address. Please try again.")


def member_exists(members: list[dict], email: str) -> bool:
    """Return True when the supplied email already belongs to a member."""
    normalized_email = email.strip().lower()

    for member in members:
        if member["email"].strip().lower() == normalized_email:
            return True
    return False


def add_member(members):
    name = get_valid_name()
    email = get_valid_email()

    if member_exists(members, email):
        print("A member with that email already exists.")
        return

    member = {
        "id": generate_next_id(members),
        "name": name,
        "email": email,
        "status": "Active",
    }

    members.append(member)
    print(f"\nThe member {member['name']} has been added successfully!")
    display_member(member)
