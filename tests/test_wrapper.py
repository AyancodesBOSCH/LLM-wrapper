import pytest

from app.wrapper import LLM
from app.schemas import validate_response


def test_valid_response():
    data = {
        "answer": "An API allows software systems to communicate.",
        "key_points": [
            "APIs define how systems communicate.",
            "APIs expose functionality.",
        ],
        "confidence": "high",
    }

    response = validate_response(data)

    assert response.answer == data["answer"]
    assert response.key_points == data["key_points"]
    assert response.confidence == "high"


def test_missing_answer():
    data = {
        "key_points": ["Point 1"],
        "confidence": "high",
    }

    with pytest.raises(ValueError):
        validate_response(data)


def test_invalid_confidence():
    data = {
        "answer": "Test",
        "key_points": ["Point 1"],
        "confidence": "invalid",
    }

    with pytest.raises(ValueError):
        validate_response(data)


def test_invalid_key_points():
    data = {
        "answer": "Test",
        "key_points": "This should be a list",
        "confidence": "high",
    }

    with pytest.raises(ValueError):
        validate_response(data)

from unittest.mock import patch

from app.wrapper import LLM
from app.schemas import validate_response


def test_llm_generate():
    fake_llm_response = """
    {
        "answer": "An API allows software systems to communicate.",
        "key_points": [
            "APIs define communication rules.",
            "APIs expose functionality."
        ],
        "confidence": "high"
    }
    """

    with patch("app.wrapper.generate_text", return_value=fake_llm_response):

        llm = LLM(
            system_prompt="You are a helpful assistant."
        )

        response = llm.generate("What is an API?")

    assert response.answer == "An API allows software systems to communicate."

    assert response.key_points == [
        "APIs define communication rules.",
        "APIs expose functionality."
    ]

    assert response.confidence == "high"

def test_llm_invalid_json():
    fake_response = "This is not JSON."

    with patch(
        "app.wrapper.generate_text",
        return_value=fake_response,
    ):
        llm = LLM()

        with pytest.raises(Exception):
            llm.generate("What is an API?")

def test_llm_invalid_schema():
    fake_response = """
    {
        "answer": "This is an answer",
        "key_points": "This should be a list",
        "confidence": "high"
    }
    """

    with patch(
        "app.wrapper.generate_text",
        return_value=fake_response,
    ):
        llm = LLM()

        with pytest.raises(Exception):
            llm.generate("What is an API?")
            