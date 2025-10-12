from nasp.llm_wrapper import LLMWrapper

if __name__ == "__main__":
    print("=== NASP SDK Demo (Improved Version) ===")
    agent = LLMWrapper()

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting demo.")
            break

        # clear and contextual prompt
        full_prompt = f"You are a concise, helpful AI assistant.\nUser: {user_input}\nAssistant:"
        response = agent.generate(full_prompt)

        print(f"Agent: {response}\n")
