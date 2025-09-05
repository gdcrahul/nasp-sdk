def block_bad_words(text: str) -> bool:
    """Return True if unsafe keywords are found in text."""
    bad_words = ["password", "attack", "hack", "credit card"]
    for word in bad_words:
        if word.lower() in text.lower():
            return True
    return False
