import json

from app.client import generate_text


class LLM:
    def __init__(self, system_prompt: str | None = None):
        self.system_prompt = system_prompt

    def generate(self, prompt: str) -> dict:
        instructions = self.system_prompt or ""

        json_instruction = """
You must return your response as valid JSON.

Return exactly this structure:

{
    "answer": "your answer here"
}

Rules:
- The response must be a JSON object.
- The object must contain an "answer" field.
- "answer" must be a string.
- Do not include Markdown.
- Do not include code fences.
- Do not include any text outside the JSON object.
"""

        full_prompt = f"""
{instructions}

{json_instruction}

User request:
{prompt}
"""

        response = generate_text(full_prompt)

        try:
            data = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "LLM returned invalid JSON."
            ) from exc

        if not isinstance(data, dict):
            raise ValueError(
                "LLM response must be a JSON object."
            )

        if "answer" not in data:
            raise ValueError(
                'LLM response is missing the "answer" field.'
            )

        if not isinstance(data["answer"], str):
            raise ValueError(
                'LLM "answer" field must be a string.'
            )

        return data