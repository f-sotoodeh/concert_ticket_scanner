def print_summary(df, session):
    print("\n--- Scan Summary ---")
    print(f"Total scanned: {session.scanned}")
    print(f"Valid tickets: {session.valid}")
    print(f"Used tickets: {session.used}")
    print(f"Invalid tickets: {session.invalid}")

    print("\n--- Ticket Statuses ---")
    print(df["status"].value_counts())