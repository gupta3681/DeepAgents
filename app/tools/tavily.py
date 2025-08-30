
import os
from typing import Literal, Dict, Any
from tavily import TavilyClient
from langchain_core.tools import tool


# Simple module-level client initialization
_tavily_client = None


def get_tavily_client() -> TavilyClient:
    """Get or create Tavily client instance"""
    global _tavily_client
    if _tavily_client is None:
        api_key = os.environ.get("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable is required")
        _tavily_client = TavilyClient(api_key=api_key)
    return _tavily_client




@tool
def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
    include_raw_content: bool = False,
) -> Dict[str, Any]:
    """Run a web search using Tavily API to find information on the internet.
    
    Args:
        query: The search query string
        max_results: Maximum number of results to return (default: 5)
        topic: Search topic category - general, news, or finance (default: general)
        include_raw_content: Whether to include raw HTML content (default: False)
        
    Returns:
        Dictionary containing search results with titles, URLs, and content
    """
    client = get_tavily_client()
    return client.search(
        query,
        max_results=max_results,
        include_raw_content=include_raw_content,
        topic=topic,
    )
