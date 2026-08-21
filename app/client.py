import os

import requests
from dotenv import load_dotenv

from app.exceptions import LLMClientError


load_dotenv()

API_KEY = os.getenv("MODEL_FARM_API_KEY")

if not API_KEY:
    raise RuntimeError("MODEL_FARM_API_KEY is not set.")


URL = (
    "https://aoai-farm.bosch-temp.com"
    "/api/openai/deployments/gpt-5-nano-2025-08-07"
    "/chat/completions"
    "?api-version=2025-04-01-preview"
)


def generate_text(prompt: str) -> str:

    try:
        response = requests.post(
            URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-5-nano-2025-08-07",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            },
            timeout=60,
        )

    except requests.RequestException as exc:
        raise LLMClientError(
            "Could not connect to Bosch Model Farm."
        ) from exc

    if response.status_code != 200:
        raise LLMClientError(
            f"Bosch Model Farm returned HTTP "
            f"{response.status_code}."
        )

    try:
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except (ValueError, KeyError, IndexError, TypeError) as exc:
        raise LLMClientError(
            "Bosch Model Farm returned an unexpected response."
        ) from exc