# Ở đây là để modify model LLM của riêng mình (OpenAI, Gemini, ChatGPT, ...)

from langchain_openai import ChatOpenAI
import os
def load_llm(model_name):
    api_key = os.getenv("OPENAPI_KEY_API")
    if not api_key:
        raise ValueError("API key for OpenAI is not set. Please set OPENAI_API_KEY in your environment.")
    if model_name == "gpt-3.5-turbo":
        return ChatOpenAI(
            model = model_name,
            temperature = 0.0,
            max_tokens = 1000,
            api_key=api_key
        )
    elif model_name == "gpt-4":
        return ChatOpenAI(
            model = model_name,
            temperature = 0.0,
            max_tokens = 1000,
            api_key=api_key
        )
    else:
        raise ValueError(
            "Unknown model.\
                Please choose from ['gpt-3.5-turbo','gpt-4']"
        )