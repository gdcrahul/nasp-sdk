class ContextFilter:
    """
    Detect unsafe queries based on context/intent.
    """
    UNSAFE_CONTEXTS = [
        "bomb", "explosive", "attack plan", "hack system",
        "illegal", "drugs", "terror", "phishing", "credit card steal"
    ]
    
    def check(self, text: str) -> bool:
        if not text:
            return False
        text_lower = text.lower()
        return any(context in text_lower for context in self.UNSAFE_CONTEXTS)
