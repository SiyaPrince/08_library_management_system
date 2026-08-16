from support_operations.displayers import display_member


def view_members(members: list[dict]) -> None:
    if not members:
        print("No members found.")
        return

    print(f"\nMembers: ({len(members)})")
    print("=" * 45)

    for number, member in enumerate(members, start=1):
        print(f"\nMember {number}")
        display_member(member)