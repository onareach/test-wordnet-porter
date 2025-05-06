# Installation Guide

This guide provides detailed instructions for installing WordNet Porter.

## Prerequisites

- Python 3.6 or higher
- PostgreSQL server (installed and running)
- SQLite WordNet database
- **Virtual Environment**: This application is designed to run in a Python virtual environment
- **psycopg2-binary**: The application specifically requires the `psycopg2-binary` package, not the standard `psycopg2` package

## Virtual Environment Setup (Important)

WordNet Porter is designed to run in a Python virtual environment. This isolates the application's dependencies from your system Python installation and prevents conflicts with other packages.

### Creating a Virtual Environment

```bash
# Create a virtual environment
python -m venv wordnet_porter_venv

# Activate the virtual environment
# On Windows:
wordnet_porter_venv\Scripts\activate
# On macOS/Linux:
source wordnet_porter_venv/bin/activate
```

You should see the virtual environment name in your command prompt, indicating it's active. All subsequent installation commands should be run with the virtual environment activated.

## Installation Methods

### Method 1: Using pip (Recommended)

The easiest way to install WordNet Porter is using pip within your activated virtual environment:

```bash
# Make sure your virtual environment is activated
pip install wordnet-porter
```

This will install the latest stable version from PyPI, including all required dependencies.

### Method 2: From Source

To install the latest development version from source:

```bash
# Clone the repository
git clone https://github.com/onareach/wordnet-porter.git
cd wordnet-porter

# Create and activate a virtual environment (if not already done)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

### Method 3: Using the Installation Script

If you've downloaded the source code, you can use the included installation script:

```bash
chmod +x install.sh
./install.sh
```

This script will:
1. Check Python version
2. Create a virtual environment
3. Install dependencies
4. Install WordNet Porter in development mode

## Important Note About Dependencies

This project specifically requires `psycopg2-binary` and not the standard `psycopg2` package. Using the standard `psycopg2` package may cause errors. The correct dependency will be installed automatically when you install the package, but if you're installing dependencies manually, make sure to use:

```bash
pip install psycopg2-binary
```

## Verifying Installation

To verify that WordNet Porter is installed correctly:

```bash
# Make sure your virtual environment is activated
wordnet-porter --help
```

This should display the help message with available options.

## Troubleshooting Installation

If you encounter issues during installation:

1. **Ensure your virtual environment is activated**
   - Check that your command prompt shows the virtual environment name
   - If not, activate it using the commands in the "Creating a Virtual Environment" section

2. **Verify psycopg2-binary is installed correctly**
   ```bash
   pip list | grep psycopg2
   ```
   - You should see `psycopg2-binary` in the list, not just `psycopg2`

3. **Check Python version compatibility**
   ```bash
   python --version
   ```
   - Ensure you're using Python 3.6 or higher

## Installing WordNet SQLite Database

WordNet Porter requires a WordNet SQLite database to migrate. If you don't have one:

1. Download the WordNet database from [WordNet's official website](https://wordnet.princeton.edu/)
2. Follow the instructions to convert it to SQLite format (if necessary)
3. Note the path to the SQLite database file

## Next Steps

Now that you have installed WordNet Porter, you can proceed to the [Usage Guide](usage.md) to learn how to use it.
