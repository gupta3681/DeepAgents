"""LLM model initialization and configuration"""

import os
from langchain_openai import ChatOpenAI
from typing import Optional

from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key() -> str:
    """Get OpenAI API key from environment"""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    return api_key

 
# GPT-4o - Latest flagship model
gpt4o = ChatOpenAI(
    model="gpt-4o",
    api_key=get_openai_api_key(),
    temperature=0.1,
    max_tokens=4096,
)

# GPT-4o Mini - Faster and more cost-effective
gpt4o_mini = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=get_openai_api_key(),
    temperature=0.1,
    max_tokens=4096,
)

# GPT-4 Turbo - Previous generation flagship
gpt4_turbo = ChatOpenAI(
    model="gpt-4-turbo",
    api_key=get_openai_api_key(),
    temperature=0.1,
    max_tokens=4096,
)

# GPT-3.5 Turbo - Legacy but still useful for simple tasks
gpt35_turbo = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=get_openai_api_key(),
    temperature=0.1,
    max_tokens=4096,
)


def get_model(model_name: str, temperature: Optional[float] = None, max_tokens: Optional[int] = None) -> ChatOpenAI:
    """Get a configured model instance
    
    Args:
        model_name: Name of the model (gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-3.5-turbo)
        temperature: Override default temperature
        max_tokens: Override default max_tokens
        
    Returns:
        Configured ChatOpenAI instance
    """
    model_config = {
        "model": model_name,
        "api_key": get_openai_api_key(),
        "temperature": temperature or 0.1,
        "max_tokens": max_tokens or 4096,
    }
    
    return ChatOpenAI(**model_config)


# Default model for general use
default_model = gpt4o_mini

# Model for complex reasoning tasks
reasoning_model = gpt4o

# Model for simple/fast tasks
fast_model = gpt4o_mini




### Other models can be added here if needed, For now only the above models are used