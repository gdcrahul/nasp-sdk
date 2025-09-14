# nasp/filters.py
import re
from typing import Pattern

class ProfanityFilter:
    """Simple profanity/unsafe-keyword filter."""
    BAD_WORDS = ["stupid", "idiot", "hack", "attack", "exploit"]

    def check(self, text: str) -> bool:
        if not text:
            return False
        lt = text.lower()
        return any(w in lt for w in self.BAD_WORDS)


class SensitiveDataFilter:
    """Detect emails, phone numbers, and sensitive keywords like 'password'."""
    KEYWORDS = ["password", "credit card", "ssn"]
    EMAIL_RE: Pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
    PHONE_RE: Pattern = re.compile(r"\b\d{10}\b")  # simple 10-digit matcher

    def check(self, text: str) -> bool:
        if not text:
            return False
        # keyword match
        lt = text.lower()
        if any(k in lt for k in self.KEYWORDS):
            return True
        # regex matches
        if self.EMAIL_RE.search(text):
            return True
        if self.PHONE_RE.search(text):
            return True
        return False


def block_bad_words(text: str) -> bool:
    """
    Legacy helper used by old code/tests.
    Returns True if text should be blocked.
    """
    return ProfanityFilter().check(text) or SensitiveDataFilter().check(text)
