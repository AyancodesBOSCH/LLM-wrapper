from app.schemas import LLMResponse


def format_response(response: LLMResponse) -> str:
    lines = [
        "Answer:",
        response.answer,
        "",
        "Key points:",
    ]

    for point in response.key_points:
        lines.append(f"- {point}")

    lines.extend(
        [
            "",
            f"Confidence: {response.confidence}",
        ]
    )

    return "\n".join(lines)