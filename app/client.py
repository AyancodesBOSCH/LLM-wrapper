import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MODEL_FARM_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "MODEL_FARM_API_KEY is not set"
    )

ENDPOINT = (
    "https://aoai-farm.bosch-temp.com/api/openai/deployments/"
    "gpt-5-nano-2025-08-07/chat/completions?api-version=2025-04-01-preview"
)


def generate_text(prompt: str) -> str:
    response = requests.post(
        ENDPOINT,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "gpt-5-nano-2025-08-07",
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
