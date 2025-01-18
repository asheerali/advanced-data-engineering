import sqlite3
import pandas as pd


def fetch_table(conn: sqlite3.Connection, table_name: str) -> pd.DataFrame:
    """
    Fetch all records from the specified table in the SQLite database.

    :param conn: sqlite3.Connection
        The connection object to the SQLite database.
    :param table_name: str
        The name of the table to fetch data from.
    :return: pd.DataFrame
        A DataFrame containing all records from the specified table.
    """
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql_query(query, conn)
    return df
