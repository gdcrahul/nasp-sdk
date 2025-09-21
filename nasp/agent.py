from .filters import ProfanityFilter, SensitiveDataFilter, block_bad_words
from .context_filter import ContextFilter
from .utils import log_event

class NASPAgent:
    def __init__(self):
        # Default filter chain: Profanity + Sensitive + Context
        self.filters = [ProfanityFilter(), SensitiveDataFilter(), ContextFilter()]
    
    def add_filter(self, filter_obj):
        """Add a new filter dynamically"""
        self.filters.append(filter_obj)
        log_event(f"Filter {filter_obj.__class__.__name__} added")

    def safe_ask(self, text: str) -> str:
        """Run all filters and return safe response or block"""
        if not isinstance(text, str):
            log_event(f"Blocked invalid input type: {text}")
            return "⚠️ [blocked] Invalid input type"
        
        for f in self.filters:
            try:
                if f.check(text):
                    log_event(f"Blocked by {f.__class__.__name__}: {text}")
                    return "⚠️ [blocked] Unsafe content detected"
            except Exception as e:
                log_event(f"Filter {f.__class__.__name__} error: {e}")
                continue
        
        # Mock LLM response (replaceable with real LLM)
        log_event(f"Safe response allowed: {text}")
        return f"This is a safe response! You asked: {text}"
