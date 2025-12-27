class Ticket:
    def __init__(self, code, status):
        self.code = code
        self.status = status

    def is_valid(self):
        return self.status == "valid"

    def mark_used(self):
        self.status = "used"


class ScanSession:
    def __init__(self):
        self.scanned = 0
        self.valid = 0
        self.used = 0
        self.invalid = 0

    def to_dict(self):
        return {
            "scanned": self.scanned,
            "valid": self.valid,
            "used": self.used,
            "invalid": self.invalid,
        }

    @classmethod
    def from_dict(cls, data):
        session = cls()
        session.scanned = data.get("scanned", 0)
        session.valid = data.get("valid", 0)
        session.used = data.get("used", 0)
        session.invalid = data.get("invalid", 0)
        return session
