import pandas as pd


REQUIRED_COLUMNS = {"code", "status"}
ALLOWED_STATUSES = {"valid", "used"}


def load_and_validate_tickets(csv_path):
    df = pd.read_csv(csv_path)

    if not REQUIRED_COLUMNS.issubset(df.columns):
        raise ValueError("CSV must contain columns: code, status")

    if df["code"].isnull().any():
        raise ValueError("Ticket code cannot be empty")

    if not set(df["status"]).issubset(ALLOWED_STATUSES):
        raise ValueError("Invalid ticket status found")

    return df