## Database Migration Tool

This repository contains two Python scripts, migration.py and rollback.py, designed to migrate a PostgreSQL database schema and rollback changes if necessary. These scripts are specifically tailored to alter the schema of tables named students and interests.

### Prerequisites
- PostgreSQL database installed and running.
- Python 3.x installed.
- psycopg2 library installed (pip install psycopg2).

### Setup
1. Ensure your PostgreSQL database is running and accessible.
2. Modify the database connection parameters (dbname, user, password, host, port) in both migration.py and rollback.py to match your PostgreSQL setup.

### Usage

#### Migration (migration.py)
- *Purpose:* This script migrates the database schema according to predefined alterations.
- *Steps:*
    1. Connects to the specified PostgreSQL database.
    2. Executes a series of SQL ALTER TABLE statements to rename columns and modify their types.
    3. Updates the interests table to concatenate similar interests for each student into an array format.
    4. Commits the changes if successful, otherwise rolls back the transaction.

#### Rollback (rollback.py)
- *Purpose:* This script rolls back the changes made by the migration script.
- *Steps:*
    1. Connects to the specified PostgreSQL database.
    2. Reverses the alterations made by the migration script, restoring the original schema.
    3. Updates the interests table to retain only one interest per student if duplicates were concatenated during migration.
    4. Commits the changes if successful, otherwise rolls back the transaction.

### Example

#### Initial Tables
- students:
    sql
    CREATE TABLE students (
        st_id SERIAL PRIMARY KEY,
        st_name VARCHAR(20),
        st_last VARCHAR(20)
    );

    INSERT INTO students (st_name, st_last) VALUES
    ('Konul', 'Gurbanova'),
    ('Shahnur', 'Isgandarli'),
    ('Natavan', 'Mammadova');
    

- interests:
    sql
    CREATE TABLE interests (
        student_id INTEGER,
        interest VARCHAR(20)
    );
    

#### Running Migration
- Execute migration.py to apply schema alterations.

#### Performing Operations
- After migration, perform operations that utilize the modified schema.

#### Rolling Back
- Execute rollback.py to revert the schema changes if needed.
