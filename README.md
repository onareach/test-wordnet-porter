# Test WordNet Porter Repository

This is a minimal test repository for troubleshooting GitHub Actions workflows for the WordNet Porter project.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the package in development mode:
   ```
   pip install -e .
   ```

3. Run the basic test:
   ```
   python -m pytest tests/test_basic.py -v
   ```

## Environment Variables

- `WORDNET_SQLITE_PATH`: Path to the SQLite WordNet database
