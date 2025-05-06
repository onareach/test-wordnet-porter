"""
Configuration handling for the WordNet Porter application.
"""

import os
import yaml
import sys
from pathlib import Path


def get_sqlite_path():
    """Get the path to the SQLite database."""
    # First check environment variable
    env_path = os.environ.get("WORDNET_SQLITE_PATH")
    if env_path and os.path.exists(env_path):
        return env_path
    
    # Default path
    default_path = os.path.expanduser("~/.wn_data/wn.db")
    return default_path


def load_config():
    """Load configuration from config.yaml."""
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}
