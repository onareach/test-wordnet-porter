#!/usr/bin/env python3
# wordnet_porter/main.py
"""
WordNet Porter - SQLite to PostgreSQL Migration Utility

This is the main entry point for the WordNet Porter application, which
coordinates the step-by-step process of migrating a WordNet SQLite database
to PostgreSQL.
"""
import sys
import logging
from typing import List, Tuple, Callable, Optional, Any, Dict, Union

from wordnet_porter.bootstrap import setup, print_header
from wordnet_porter.config import config
from wordnet_porter.cli import validate_cli_args, parse_cli_args, show_help

# Set up logging
logger = logging.getLogger(__name__)

# Import all steps
from wordnet_porter.steps import (
    step010_test_sqlite_connection,
    step020_postgres_credentials,
    step030_create_postgres_database,
    step035_purge_directories,
    step040_extract_sqlite_schema,
    step045_analyze_dependencies,
    step050_extract_sqlite_metadata,
    step060_generate_tables,
    step065_generate_foreign_keys,
    step067_generate_foreign_key_validators,
    step068_generate_indexes,
    step070_run_table_scripts,
    step080_run_index_scripts,
    step090_insert_data_tables,
    step095_validate_foreign_key_data,
    step100_apply_foreign_keys
)

# Type alias for a step function
StepFunction = Callable[[], bool]
# Type alias for a step definition (description and function)
StepDefinition = Tuple[str, StepFunction]

def main() -> None:
    """
    Main function to coordinate the WordNet migration process.
    
    This function:
    1. Processes command-line arguments
    2. Sets up the environment
    3. Executes the selected migration steps
    4. Reports on the success or failure of the migration
    """
    logger.info("Starting WordNet Porter")
    
    # Validate command-line arguments
    logger.info("Validating command-line arguments")
    validate_cli_args()
    
    # Define all steps with descriptions
    ALL_STEPS: List[StepDefinition] = [
        ("Step 1:  Test SQLite Database Connection", step010_test_sqlite_connection.run),
        ("Step 2:  Login to PostgreSQL", step020_postgres_credentials.run),
        ("Step 3:  Create WordNet Database in PostgreSQL", step030_create_postgres_database.run),
        ("Step 4:  Purge Directories", step035_purge_directories.run),
        ("Step 5:  Extract SQLite Schema", step040_extract_sqlite_schema.run),
        ("Step 6:  Analyze Dependencies", step045_analyze_dependencies.run),
        ("Step 7:  Extract SQLite Metadata", step050_extract_sqlite_metadata.run),
        ("Step 8:  Generate Table Scripts", step060_generate_tables.run),
        ("Step 9:  Generate Foreign Key Scripts", step065_generate_foreign_keys.run),
        ("Step 10: Generate Foreign Key Validators", step067_generate_foreign_key_validators.run),
        ("Step 11: Generate Index Scripts", step068_generate_indexes.run),
        ("Step 12: Run Table Creation Scripts", step070_run_table_scripts.run),
        ("Step 13: Run Index Creation Scripts", step080_run_index_scripts.run),
        ("Step 14: Insert Data into Tables", step090_insert_data_tables.run),
        ("Step 15: Validate Foreign Key Data", step095_validate_foreign_key_data.run),
        ("Step 16: Apply Foreign Keys", step100_apply_foreign_keys.run),
    ]
    
    # Parse command-line arguments to determine which steps to run
    logger.info("Parsing command-line arguments to determine steps to run")
    start_index, end_index, only_step = parse_cli_args(ALL_STEPS)
    
    # Setup environment first
    logger.info("Setting up environment")
    print_header("Setting up environment...")
    setup()
    if not config.success:
        logger.error("Bootstrap failed")
        exit("❌ Bootstrap failed - please fix the issues before continuing.")
    
    # Run the selected steps
    if only_step is not None:
        # Run only one specific step
        step_desc = ALL_STEPS[only_step][0]
        step_func = ALL_STEPS[only_step][1]
        
        logger.info(f"Running single step: {step_desc}")
        print_header(f"Running {step_desc}")
        
        step_func()
        
        if not config.success:
            logger.error(f"Step failed: {step_desc}")
    else:
        # Run a range of steps
        logger.info(f"Running steps {start_index+1} through {end_index}")
        
        for i, (step_desc, step_func) in enumerate(ALL_STEPS[start_index:end_index], start=start_index+1):
            logger.info(f"Starting step {i}: {step_desc}")
            print_header(f"{step_desc}")
            
            step_func()
            
            if not config.success:
                logger.error(f"Step {i} failed: {step_desc}")
                print(f"\n❌ Stopping after {step_desc} due to error.")
                exit(1)
            
            logger.info(f"Completed step {i}: {step_desc}")
    
    # Report final status
    if config.success:
        logger.info("All selected steps completed successfully")
        print("\n✅ All selected steps completed successfully!")
    else:
        logger.error("One or more steps failed")
        print("\n❌ One or more steps failed. See above for details.")
        exit(1)

if __name__ == "__main__":
    main()
