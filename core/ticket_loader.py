import pandas as pd


def load_and_validate_tickets(csv_path) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    if df.empty:
        raise ValueError("CSV file is empty")
    if not all(df.columns == ["code", "category", "status"]):
        raise ValueError("CSV file has incorrect columns")
    return df
