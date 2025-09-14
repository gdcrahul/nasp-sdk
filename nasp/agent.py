# nasp/agent.py
from .filters import ProfanityFilter, SensitiveDataFilter, block_bad_words

class NASPAgent:
    def __init__(self):
        # default filter chain
        self.filters = [ProfanityFilter(), SensitiveDataFilter()]

    def add_filter(self, filter_obj):
        """Add a new filter object (must implement check(text)->bool)."""
        self.filters.append(filter_obj)

    def safe_ask(self, text: str) -> str:
        """
        Run each filter's check(); if any filter returns True => block.
        Return a human-friendly blocked message or a safe response.
        """
        if not isinstance(text, str):
            return "[blocked] Invalid input type"

        # run filters
        for f in self.filters:
            try:
                if f.check(text):
                    return "[blocked] Unsafe content detected"
            except Exception:
                # if a filter errors, continue (robustness)
                continue

        # mock/placeholder LLM response — replace with real LLM later
        return f"This is a safe response! You asked: {text}"
