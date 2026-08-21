class LLMError(Exception):
    """Base exception for the LLM wrapper."""


class LLMResponseError(LLMError):
    """Raised when the LLM response cannot be parsed or validated."""


class LLMClientError(LLMError):
    """Raised when communication with Bosch Model Farm fails."""