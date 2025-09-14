# demo.py
from nasp.agent import NASPAgent

def main():
    agent = NASPAgent()
    print("=== NASP SDK Demo (Week 2) ===")

    examples = [
        "Hello, how are you?",
        "My email is test@example.com and my phone is 9876543210",
        "Can you help me hack a system?",
        "Tell me a fun fact about space."
    ]

    for prompt in examples:
        print("\nUser:", prompt)
        print("Agent:", agent.safe_ask(prompt))

if __name__ == "__main__":
    main()
