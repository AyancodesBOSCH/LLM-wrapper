import json

from app.client import generate_text
from app.exceptions import LLMResponseError, LLMClientError
from app.prompts import JSON_RESPONSE_INSTRUCTIONS
from app.schemas import validate_response


class LLM:

    def __init__(self, system_prompt: str | None = None):
        self.system_prompt = system_prompt

    def generate(self, prompt: str):

        instructions = self.system_prompt or ""

        full_prompt = f"""
{instructions}

{JSON_RESPONSE_INSTRUCTIONS}

User request:
{prompt}
"""

        response = generate_text(full_prompt)

        try:
            data = json.loads(response)
        except json.JSONDecodeError as exc:
            raise LLMResponseError(
                "LLM returned invalid JSON."
            ) from exc

        try:
            return validate_response(data)
        except ValueError as exc:
            raise LLMResponseError(
                "LLM returned JSON with an invalid structure."
            ) from exc