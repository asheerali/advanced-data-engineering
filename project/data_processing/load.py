import sqlite3
import pandas as pd

'''
To load data into sql lite database
'''
def LoadDfToSqlite(db_name: str, table_name: str, df: pd.DataFrame) -> None:
    '''
    Parameters:
        db_name - Name of the SQLite database file
        table_name - Name of the table to which the DataFrame will be loaded
        df - DataFrame containing the data to be loaded into the SQLite table

    Returns:
        None
    '''
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()