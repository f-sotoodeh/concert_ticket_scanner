import json
from pathlib import Path
from core.models import ScanSession


SESSION_FILE = Path("data/session_history.json")


def create_new_session():
    return ScanSession()


def save_session(session):
    with open(SESSION_FILE, "w") as f:
        json.dump(session.to_dict(), f)


def load_session():
    if not SESSION_FILE.exists():
        return ScanSession()

    with open(SESSION_FILE, "r") as f:
        data = json.load(f)
        return ScanSession.from_dict(data)


def reset_session():
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()
