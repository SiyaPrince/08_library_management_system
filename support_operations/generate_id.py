# Generate the next unique ID for a new record based on existing records.

def generate_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1