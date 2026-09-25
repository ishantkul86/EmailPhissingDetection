import os


LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama",
)

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "",
)