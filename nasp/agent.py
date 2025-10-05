from .filters import ProfanityFilter, SensitiveDataFilter, block_bad_words
from .context_filter import ContextFilter
from .utils import log_event
from .llm_wrapper import LLMWrapper

class NASPAgent:
    def __init__(self):
        # Input gates (before LLM)
        self.input_filters = [ProfanityFilter(), SensitiveDataFilter(), ContextFilter()]

        # Output gates (after LLM)
        self.output_filters = [SensitiveDataFilter(), ProfanityFilter()]

        # LLM wrapper
        self.llm = LLMWrapper()

    def add_input_filter(self, filter_obj):
        self.input_filters.append(filter_obj)
        log_event(f"Input filter {filter_obj.__class__.__name__} added")

    def add_output_filter(self, filter_obj):
        self.output_filters.append(filter_obj)
        log_event(f"Output filter {filter_obj.__class__.__name__} added")

    def safe_ask(self, text: str) -> str:
        """Full pipeline: Input → LLM → Output"""

        # Input validation
        if not isinstance(text, str):
            log_event("Invalid input type")
            return "⚠️ [blocked] Invalid input type"

        # Input filters
        for f in self.input_filters:
            if f.check(text):
                log_event(f"Blocked by {f.__class__.__name__} (input)")
                return "⚠️ [blocked] Unsafe input detected"

        # Pass to LLM
        raw_output = self.llm.generate(text)

        # Output filters
        for f in self.output_filters:
            if f.check(raw_output):
                log_event(f"Blocked/redacted by {f.__class__.__name__} (output)")
                return "⚠️ [blocked/redacted] Unsafe LLM output detected"

        log_event(f"Safe output returned")
        return raw_output
