import json
from pathlib import Path
from typing import Dict

from core.session import ScanSession


def save_scan_history(entry: Dict, history_path: Path):
    history_path.parent.mkdir(parents=True, exist_ok=True)

    raw_history = []
    if history_path.exists():
        with open(history_path, "r") as f:
            raw_history = json.load(f)

    raw_history.append(entry)

    with open(history_path, "w") as f:
        json.dump(raw_history, f, indent=2)


def load_session_history(history_path: Path) -> ScanSession:
    """Load history from JSON and populate a ScanSession object."""
    session = ScanSession()

    if history_path.exists():
        with open(history_path, "r") as f:
            history = json.load(f)

        for entry in history:
            # Map decision to simple string for record_scan
            reason = entry.get("reason")
            if reason:
                if "not found" in reason.lower():
                    decision_str = "not found"
                elif "used" in reason.lower():
                    decision_str = "already used"
                elif "format" in reason.lower():
                    decision_str = "invalid format"
                else:
                    decision_str = "rejected"
            else:
                decision_str = "accepted"

            session.record_scan(entry["code"], decision_str)

    return session
