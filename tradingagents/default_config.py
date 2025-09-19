import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "data_dir": "/mnt/c/Users/wujun/Documents/Code/ScAI/FR1-data",
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": "google",
    "deep_think_llm": "gemini-2.5-flash",
    "quick_think_llm": "gemini-2.5-flash",
    "backend_url": "https://generativelanguage.googleapis.com/v1",
    "google_api_key": "AIzaSyAKuBDKfaUC5r4ja1odguYhbe1zF_SIZOw",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Tool settings
    "online_tools": True,
}
