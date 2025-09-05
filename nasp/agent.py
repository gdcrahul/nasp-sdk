from .filters import block_bad_words

class NASPAgent:
    def __init__(self):
        pass  # no special setup yet

    def safe_ask(self, text: str) -> str:
        """Check input and block unsafe queries."""
        if block_bad_words(text):
            return "⚠️ Unsafe content blocked"
        return "This is a safe response!"
