import re
from typing import Pattern

class ProfanityFilter:
    BAD_WORDS = ["stupid", "idiot", "hack", "attack", "exploit"]
    
    def check(self, text: str) -> bool:
        if not text:
            return False
        text_lower = text.lower()
        return any(word in text_lower for word in self.BAD_WORDS)

class SensitiveDataFilter:
    KEYWORDS = ["password", "credit card", "ssn"]
    EMAIL_RE: Pattern = re.compile(r"[\w\.-]+@[\w\.-]+\.\w+")
    PHONE_RE: Pattern = re.compile(r"\b\d{10}\b")
    
    def check(self, text: str) -> bool:
        if not text:
            return False
        text_lower = text.lower()
        if any(k in text_lower for k in self.KEYWORDS):
            return True
        if self.EMAIL_RE.search(text) or self.PHONE_RE.search(text):
            return True
        return False

def block_bad_words(text: str) -> bool:
    """Legacy helper for backward compatibility."""
    return ProfanityFilter().check(text) or SensitiveDataFilter().check(text)
