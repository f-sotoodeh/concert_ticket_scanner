import json
from pathlib import Path
from typing import Dict, List

from core.session import ScanSession

# HISTORY_FILE = Path("data/session_history.json")


# HISTORY_FILE = Path("data/session_history.json")  # Remove this

# # In save_scan_history and load_session_history, pass history_path as arg
# def save_scan_history(entry: Dict, history_path: Path):
#     history_path.parent.mkdir(parents=True, exist_ok=True)
#     history = load_session_history(history_path)  # Reuse load
#     history.append(entry)
#     with open(history_path, "w") as f:
#         json.dump(history, f, indent=2)

# def load_session_history(history_path: Path) -> List[Dict]:
#     if history_path.exists():
#         with open(history_path, "r") as f:
#             return json.load(f)
#     return []


# def save_scan_history(entry: Dict, history_path: Path):
#     """Append a scan entry to the history JSON file."""
#     history_path.parent.mkdir(parents=True, exist_ok=True)

#     if HISTORY_FILE.exists():
#         with open(HISTORY_FILE, "r") as f:
#             history: List[Dict] = json.load(f)
#     else:
#         history = []

#     history.append(entry)

#     with open(HISTORY_FILE, "w") as f:
#         json.dump(history, f, indent=2)


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
            # decision = entry["decision"]  # "accepted" or "rejected"
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
