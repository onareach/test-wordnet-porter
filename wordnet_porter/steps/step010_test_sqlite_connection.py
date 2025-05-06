"""
Step 010: Test SQLite Connection.
"""

import os
import sqlite3
import sys

from .. import config


def run():
    """Run this step."""
    print("Step 010: Testing SQLite Connection")
    print("-" * 50)
    
    sqlite_path = config.get_sqlite_path()
    print(f"SQLite database path: {sqlite_path}")
    
    if not os.path.exists(sqlite_path):
        print(f"Error: SQLite database not found at {sqlite_path}")
        print("Please set the WORDNET_SQLITE_PATH environment variable to the correct path.")
        return 1
    
    try:
        conn = sqlite3.connect(sqlite_path)
        cursor = conn.cursor()
        
        # Get SQLite version
        cursor.execute("SELECT sqlite_version();")
        version = cursor.fetchone()
        print(f"SQLite version: {version[0]}")
        
        # Test a simple query
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 5;")
        tables = cursor.fetchall()
        
        if tables:
            print("Found tables:")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("No tables found in the database.")
        
        conn.close()
        print("SQLite connection test successful.")
        return 0
    
    except sqlite3.Error as e:
        print(f"SQLite connection error: {e}")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
