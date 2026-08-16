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
            print("Email cannot be empty.")

def member_exists(
    members: list[dict],
    name: str,
    email: str,
) -> bool:
    """Return True if the same member already exists."""

    normalized_name = name.strip().lower()
    normalized_email = email.strip().lower()

    for member in members:
        if (
            member["name"].strip().lower() == normalized_name
            and member["email"].strip().lower() == normalized_email
        ):
            print("Member already exists.")
            return True
    return False

def add_member(members):

    # Ask for inputs

    name = get_valid_name()
    email = get_valid_email()

    if member_exists(members, name, email):
         return

    member_id = generate_next_id(members)

    member_id = generate_next_id(members)

    # Add to dictionary
    member = {
        "id": member_id,
        "name": name,
        "email": email,
        "status": "Active"
    }

    members.append(member)

    print(f"\nThe member {member['name']} has been added successfully!!")

    display_member(member)


