def interactive_scan(df, session):
    codes = set(df["code"])

    while True:
        user_input = input("Scan ticket code: ").strip()

        if user_input.lower() == "quit":
            break

        session.scanned += 1

        if user_input not in codes:
            print("Invalid ticket")
            session.invalid += 1
            continue

        row = df.loc[df["code"] == user_input].iloc[0]

        if row["status"] == "used":
            print("Ticket already used")
            session.used += 1
        else:
            print("Ticket valid")
            session.valid += 1
            df.loc[df["code"] == user_input, "status"] = "used"
