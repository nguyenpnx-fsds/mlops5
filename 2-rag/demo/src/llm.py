from langchain.chat_models import init_chat_model
from settings import SETTINGS

llm = init_chat_model(
    "gpt-4o-mini",
    api_key=SETTINGS.OPENAI_API_KEY,
    temperature=0.7,
    model_provider="openai",
)
