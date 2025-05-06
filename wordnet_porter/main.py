#!/usr/bin/env python3
"""
Main entry point for the WordNet Porter application.
"""

import argparse
import sys
import os

from . import __version__
from . import config
from . import bootstrap


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(description="WordNet to PostgreSQL Porting Tool")
    parser.add_argument('--version', action='store_true', help='Show version information')
    parser.add_argument('--help_all', action='store_true', help='Show detailed help information')
    parser.add_argument('--step_list', action='store_true', help='List available steps')
    parser.add_argument('--only_step', type=int, help='Run only the specified step')
    
    args = parser.parse_args()
    
    if args.version:
        print(f"WordNet Porter v{__version__}")
        return 0
    
    if args.help_all:
        print("WordNet to PostgreSQL Porting Tool - Detailed Help")
        print("=" * 50)
        print("This tool helps you port WordNet from SQLite to PostgreSQL.")
        print("For more information, see the documentation.")
        return 0
    
    if args.step_list:
        print("Available Steps:")
        print("=" * 50)
        print("1. Test SQLite Connection")
        print("2. Get PostgreSQL Credentials")
        print("3. Create PostgreSQL Database")
        return 0
    
    if args.only_step:
        if args.only_step == 1:
            from .steps import step010_test_sqlite_connection
            return step010_test_sqlite_connection.run()
        else:
            print(f"Step {args.only_step} not implemented yet.")
            return 1
    
    # Default behavior
    print("WordNet to PostgreSQL Porting Tool")
    print(f"Version: {__version__}")
    print("Use --help for available options")
    return 0


if __name__ == "__main__":
    sys.exit(main())
