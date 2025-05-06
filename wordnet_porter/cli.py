"""
Command-line interface for the WordNet Porter application.
"""

import sys
import argparse

from . import __version__


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="WordNet to PostgreSQL Porting Tool")
    parser.add_argument('--version', action='store_true', help='Show version information')
    parser.add_argument('--help_all', action='store_true', help='Show detailed help information')
    parser.add_argument('--step_list', action='store_true', help='List available steps')
    parser.add_argument('--only_step', type=int, help='Run only the specified step')
    
    return parser.parse_args()
