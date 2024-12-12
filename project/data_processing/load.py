import sqlite3
import pandas as pd
import os

def LoadDfToSqlite(db_name: str, table_name: str, df: pd.DataFrame) -> None:
    """
    Loads data into a SQLite database.

    Parameters:
        db_name (str): Name of the SQLite database file.
        table_name (str): Name of the table to which the DataFrame will be loaded.
        df (pd.DataFrame): DataFrame containing the data to be loaded into the SQLite table.

    Returns:
        None
    """
    try:
        # Ensure the directory for the database file exists
        db_dir = os.path.dirname(db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
            print(f"Created directory for database: {db_dir}")

        # Connecting to SQLite database
        print(f"Connecting to database: {db_name}")
        conn = sqlite3.connect(db_name)

        # Loading data into the specified table
        print(f"Loading data into table: {table_name}")
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"Data successfully loaded into table: {table_name}")
    except sqlite3.OperationalError as e:
        print(f"OperationalError occurred while connecting to the database: {e}")
        raise
    except ValueError as e:
        print(f"ValueError occurred while loading data into the table: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise
    finally:
        # Closing the connection
        if 'conn' in locals():
            conn.close()
            print(f"Connection to database {db_name} closed.")
