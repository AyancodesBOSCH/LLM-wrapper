from app.client import generate_text


def main():
    prompt = input("You: ")

    try:
        response = generate_text(prompt)
        print("\nBosch Model Farm:")
        print(response)

    except Exception as e:
        print("\nERROR:")
        print(type(e).__name__)
        print(e)


if __name__ == "__main__":
    main()