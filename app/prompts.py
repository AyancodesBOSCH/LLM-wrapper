JSON_RESPONSE_INSTRUCTIONS = """
You must return your response as valid JSON.

Return exactly this structure:

{
    "answer": "your main answer here",
    "key_points": [
        "important point 1",
        "important point 2"
    ],
    "confidence": "high"
}

Rules:
- The response must be a JSON object.
- "answer" must be a string.
- "key_points" must be an array of strings.
- "confidence" must be exactly one of:
  "high", "medium", "low".
- Do not include Markdown.
- Do not include code fences.
- Do not include any text outside the JSON object.
"""