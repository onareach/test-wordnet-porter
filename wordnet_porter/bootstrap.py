"""
Bootstrap functionality for the WordNet Porter application.
"""

import os
import sys
from pathlib import Path

from . import config


def initialize():
    """Initialize the application."""
    # Check if SQLite database exists
    sqlite_path = config.get_sqlite_path()
    if not os.path.exists(sqlite_path):
        print(f"SQLite database not found at {sqlite_path}")
        print("Please set the WORDNET_SQLITE_PATH environment variable to the correct path.")
        return False
    
    return True
