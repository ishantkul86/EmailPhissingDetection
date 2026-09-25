from .base import LLMProvider
from .ollama_provider import OllamaProvider


def create_llm_provider(
    provider: str,
    model: str,
) -> LLMProvider:

    if provider == "ollama":
        return OllamaProvider(model)

    raise ValueError(
        f"Unsupported LLM provider: {provider}"
    )