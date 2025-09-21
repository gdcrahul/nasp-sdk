import datetime

def log_event(event: str):
    """Log blocked or allowed events with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {event}")
