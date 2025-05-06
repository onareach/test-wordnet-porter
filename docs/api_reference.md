# API Reference

This document provides a reference for the WordNet Porter API.

## Main Modules

### wordnet_porter.config

The configuration module handles loading and managing configuration settings.

#### Classes

##### `Config`

The main configuration class for WordNet Porter.

###### Methods

- `__init__()`: Initialize configuration with default values and load from files.
- `_load_config()`: Load configuration from files.
- `_update_nested_dict(d, u)`: Update a nested dictionary with values from another dictionary.
- `_setup_paths()`: Set up paths based on configuration.
- `_setup_file_logging()`: Set up file logging for the application.
- `setup_console_logging()`: Set up console logging if show_console_logs is True.
- `save_config()`: Save current configuration to user config file.
- `prompt_credentials()`: Prompt for PostgreSQL credentials.
- `ensure_pg_credentials()`: Ensure PostgreSQL credentials are available, prompting if necessary.

###### Properties

- `SQLITE_PATH`: Get/set SQLite database path.
- `PG_HOST`: Get/set PostgreSQL host.
- `PG_PORT`: Get/set PostgreSQL port.
- `PG_DATABASE`: Get/set PostgreSQL database name.
- `pg_user`: Get/set PostgreSQL username.
- `pg_password`: Get/set PostgreSQL password.
- `SHOW_DB_NAME`: Get/set show database name setting.
- `SHOW_LOGGING`: Get/set show logging setting.
- `MAX_LOGIN_ATTEMPTS`: Get/set maximum login attempts.
- `BATCH_SIZE`: Get/set batch size.
- `force_mode`: Get/set force mode setting.

### wordnet_porter.cli

The command-line interface module handles command-line argument parsing and validation.

#### Functions

- `show_help()`: Display help information and exit.
- `validate_cli_args()`: Validate command-line arguments.
- `parse_cli_args(all_steps)`: Parse command-line arguments and determine which steps to run.

### wordnet_porter.main

The main module coordinates the step-by-step process of migrating a WordNet SQLite database to PostgreSQL.

#### Functions

- `main()`: Main function to coordinate the WordNet migration process.

### wordnet_porter.bootstrap

The bootstrap module handles setting up the environment for the WordNet Porter application.

#### Functions

- `setup()`: Set up the environment for the WordNet Porter application.
- `print_header(message)`: Print a header message.

## Step Modules

Each step in the migration process is implemented as a separate module in the `steps` directory.

### wordnet_porter.steps.step010_test_sqlite_connection

Tests the connection to the SQLite database.

#### Functions

- `run()`: Run the step to test the SQLite database connection.

### wordnet_porter.steps.step020_postgres_credentials

Sets up PostgreSQL credentials.

#### Functions

- `run()`: Run the step to set up PostgreSQL credentials.
- `get_credentials()`: Get PostgreSQL credentials from the user.

### wordnet_porter.steps.step030_create_postgres_database

Creates the WordNet database in PostgreSQL.

#### Functions

- `run()`: Run the step to create the PostgreSQL database.

### wordnet_porter.steps.step035_purge_directories

Purges output directories if needed.

#### Functions

- `run()`: Run the step to purge directories.

### wordnet_porter.steps.step040_extract_sqlite_schema

Extracts the schema from the SQLite database.

#### Functions

- `run()`: Run the step to extract the SQLite schema.

### wordnet_porter.steps.step045_analyze_dependencies

Analyzes table dependencies.

#### Functions

- `run()`: Run the step to analyze dependencies.

### wordnet_porter.steps.step050_extract_sqlite_metadata

Extracts metadata from the SQLite database.

#### Functions

- `run()`: Run the step to extract SQLite metadata.

### wordnet_porter.steps.step060_generate_tables

Generates table creation scripts.

#### Functions

- `run()`: Run the step to generate table scripts.

### wordnet_porter.steps.step065_generate_foreign_keys

Generates foreign key creation scripts.

#### Functions

- `run()`: Run the step to generate foreign key scripts.

### wordnet_porter.steps.step067_generate_foreign_key_validators

Generates foreign key validator scripts.

#### Functions

- `run()`: Run the step to generate foreign key validators.

### wordnet_porter.steps.step068_generate_indexes

Generates index creation scripts.

#### Functions

- `run()`: Run the step to generate index scripts.

### wordnet_porter.steps.step070_run_table_scripts

Runs table creation scripts.

#### Functions

- `run()`: Run the step to execute table creation scripts.

### wordnet_porter.steps.step080_run_index_scripts

Runs index creation scripts.

#### Functions

- `run()`: Run the step to execute index creation scripts.

### wordnet_porter.steps.step090_insert_data_tables

Inserts data into tables.

#### Functions

- `run()`: Run the step to insert data into tables.
- `list_tables()`: List all tables that can be inserted.

### wordnet_porter.steps.step095_validate_foreign_key_data

Validates foreign key data.

#### Functions

- `run()`: Run the step to validate foreign key data.

### wordnet_porter.steps.step100_apply_foreign_keys

Applies foreign keys.

#### Functions

- `run()`: Run the step to apply foreign keys.

## Utility Modules

### wordnet_porter.utils.db_utils

Utility functions for database operations.

#### Functions

- `connect_to_sqlite(db_path)`: Connect to a SQLite database.
- `connect_to_postgres(host, port, database, user, password)`: Connect to a PostgreSQL database.
- `execute_query(connection, query, params=None)`: Execute a query on a database connection.
- `fetch_all(connection, query, params=None)`: Fetch all results from a query.
- `fetch_one(connection, query, params=None)`: Fetch one result from a query.
- `close_connection(connection)`: Close a database connection.
