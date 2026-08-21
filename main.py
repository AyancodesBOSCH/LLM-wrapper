from app.wrapper import LLM
from app.formatter import format_response
from app.exceptions import LLMError


def main():

    llm = LLM(
        system_prompt=(
            "You are a helpful assistant. "
            "Answer clearly and concisely."
        )
    )

    prompt = input("You: ")

    try:
        response = llm.generate(prompt)
        print("\nBosch Model Farm:")
        print(format_response(response))

    except LLMError as exc:
        print(f"\nError: {exc}")


if __name__ == "__main__":
    main()