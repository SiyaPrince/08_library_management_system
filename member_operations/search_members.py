from member_operations.view_members import view_members

def search_members(members: list[dict]) -> None:
    if not members:
        print("No members found.")
        return

    search_term = input(
        "Enter the name or email to search for: "
    ).strip().lower()

    if not search_term:
        print("Search value cannot be empty.")
        return

    found_members = []
    for member in members:
        searchable_values = (
            member["name"].lower(),
            member["email"].lower(),
        )
        if any(search_term in value for value in searchable_values):
            found_members.append(member)

    if not found_members:
        print("Member not found.")
        return

    print(f"Found {len(found_members)} matching member(s).")
    
    view_members(found_members)