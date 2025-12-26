import pandas as pd

from core.session import ScanSession


def print_summary(df: pd.DataFrame, session: ScanSession) -> None:
    """
    Print session statistics and overall ticket status summary.
    """
    print("\n== Session Summary ==")
    counts = session.get_summary()
    print(f"   Accepted:     {counts['accepted']}")
    print(f"   Rejected:     {counts['rejected']}")
    print(f"   Not found:    {counts['not_found']}")
    print(f"   Already used: {counts['already_used']}")
    print(f"   Other:        {counts['other']}")

    print("\n== Overall Ticket Statistics ==")
    status_counts = df["status"].value_counts()
    for status, count in status_counts.items():
        print(f"   {str(status).capitalize():<14} {count}")
    print(f"   Total tickets: {len(df)}")
    print()
