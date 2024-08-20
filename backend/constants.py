import os.path
from dotenv import load_dotenv

# .env 파일 환경변수 로드
load_dotenv()

OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
"""OpenAI API Key"""

OLLAMA_HOST = os.environ.get("OLLAMA_HOST")
"""Ollama Host Server Address [IP Address:Port]"""

OPENAI_MODELS = [
    "gpt-4o",
    "gpt-4o-mini",
]
"""OpenAI 모델"""

OLLAMA_MODELS = [
    "Gemma2",
    "EEVE",
    "qwen2",
]
"""Ollama 모델"""

OPENAI_MODEL_COST_PER_1K_TOKENS = {
    # GPT-4o-mini input
    "gpt-4o-mini": 0.00015,
    "gpt-4o-mini-2024-07-18": 0.00015,
    # GPT-4o-mini output
    "gpt-4o-mini-completion": 0.0006,
    "gpt-4o-mini-2024-07-18-completion": 0.0006,
    # GPT-4o input
    "gpt-4o": 0.005,
    "gpt-4o-2024-05-13": 0.005,
    # GPT-4o output
    "gpt-4o-completion": 0.015,
    "gpt-4o-2024-05-13-completion": 0.015,
}
"""OpenAI Model 1,000 토큰당 비용"""