from app.client import generate_text


class LLM:
    def generate(self, prompt: str) -> str:
        return generate_text(prompt)