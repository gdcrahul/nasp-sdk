from nasp.agent import NASPAgent

def main():
    agent = NASPAgent()

    print("=== NASP SDK Demo ===")

    # Unsafe query test
    query1 = "What is the password?"
    print(f"\nUser: {query1}")
    print("Agent:", agent.safe_ask(query1))

    # Safe query test
    query2 = "Tell me a fun fact."
    print(f"\nUser: {query2}")
    print("Agent:", agent.safe_ask(query2))

if __name__ == "__main__":
    main()
