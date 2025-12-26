# session.py
from datetime import datetime
from typing import Dict


class ScanSession:
    """Tracks statistics for the current scanning session (in-memory only)."""

    def __init__(self):
        self.start_time = datetime.now()
        self.counts: Dict[str, int] = {
            "accepted": 0,
            "rejected": 0,
            "not_found": 0,
            "already_used": 0,
            "other": 0,
        }

    def record_scan(self, code: str, decision: str):
        """Record a scan attempt based on decision."""
        decision_key = {
            "accepted": "accepted",
            "rejected": "rejected",
            "not found": "not_found",
            "already used": "already_used",
            "invalid format": "invalid_format",
        }.get(decision.lower(), "other")

        self.counts[decision_key] += 1

    def get_summary(self) -> Dict:
        """Return current session statistics."""
        return self.counts.copy()
