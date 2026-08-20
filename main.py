from app.wrapper import LLM


def main():
    llm = LLM(
        system_prompt=(
            "You are a helpful assistant. "
            "Answer clearly and concisely."
        )
    )

    prompt = input("You: ")

    response = llm.generate(prompt)

    print("\nParsed response:")
    print(response)

    print("\nAnswer:")
    print(response["answer"])


if __name__ == "__main__":
    main()