class LLMResponse:
    def __init__(
        self,
        answer: str,
        key_points: list[str],
        confidence: str,
    ):
        self.answer = answer
        self.key_points = key_points
        self.confidence = confidence


def validate_response(data: dict) -> LLMResponse:

    if not isinstance(data, dict):
        raise ValueError(
            "LLM response must be a JSON object."
        )

    if not isinstance(data.get("answer"), str):
        raise ValueError(
            '"answer" must be a string.'
        )

    if not isinstance(data.get("key_points"), list):
        raise ValueError(
            '"key_points" must be a list.'
        )

    if not all(
        isinstance(point, str)
        for point in data["key_points"]
    ):
        raise ValueError(
            'Every "key_points" item must be a string.'
        )

    if data.get("confidence") not in {
        "high",
        "medium",
        "low",
    }:
        raise ValueError(
            '"confidence" must be high, medium, or low.'
        )

    return LLMResponse(
        answer=data["answer"],
        key_points=data["key_points"],
        confidence=data["confidence"],
    )