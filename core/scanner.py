from datetime import datetime

import pandas as pd

from core.history import save_scan_history  # assuming you have this


def interactive_scan(df: pd.DataFrame, session, history_path):
    """
    Interactive ticket scanning loop.
    """
    print("Scan mode active. Enter ticket code (or 'quit'/'q' to exit):")

    while True:
        code = input("> ").strip().upper()

        if code.lower() in ["quit", "q"]:
            break

        if not code:
            print("Empty code. Try again.")
            continue

        ticket_row = df[df["code"] == code]

        if ticket_row.empty:
            decision = "rejected"
            reason = "Not found"
            print(f"{code} → Not found")
        elif ticket_row.iloc[0]["status"] != "unused":
            current_status = ticket_row.iloc[0]["status"]
            decision = "rejected"
            reason = f"Already {current_status}"
            print(f"{code} → Already {current_status}")
        else:
            df.loc[df["code"] == code, "status"] = "used"
            decision = "accepted"
            reason = None
            category = ticket_row.iloc[0]["category"]
            print(f"{code} ({category}) → Welcome!")

        # Record in session and history
        session.record_scan(
            code, decision.split("_")[0] if "_" in decision else decision
        )
        save_scan_history(
            {
                "timestamp": datetime.now().isoformat(),
                "code": code,
                "decision": decision,
                "reason": reason,
                "category": ticket_row.iloc[0]["category"]
                if not ticket_row.empty
                else None,
            },
            history_path,
        )
