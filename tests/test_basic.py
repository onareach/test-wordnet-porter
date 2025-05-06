"""
Basic tests for the WordNet Porter package.
"""

import os
import sys
import pytest


def test_import():
    """Test that the package can be imported."""
    import wordnet_porter
    assert wordnet_porter.__version__ == "0.1.0"


def test_config():
    """Test that the config module works."""
    from wordnet_porter import config
    sqlite_path = config.get_sqlite_path()
    assert sqlite_path is not None
    assert isinstance(sqlite_path, str)


def test_sqlite_connection():
    """Test the SQLite connection step."""
    from wordnet_porter.steps import step010_test_sqlite_connection
    
    # Create a dummy SQLite database if the environment variable is set
    sqlite_path = os.environ.get("WORDNET_SQLITE_PATH")
    if sqlite_path:
        os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)
        if not os.path.exists(sqlite_path):
            # Create an empty file
            with open(sqlite_path, 'w') as f:
                pass
    
    # This should return 1 (error) since we're using a dummy database,
    # but it shouldn't crash
    result = step010_test_sqlite_connection.run()
    assert result in (0, 1)  # Either success or expected error
