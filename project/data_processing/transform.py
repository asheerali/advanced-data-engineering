import pandas as pd

'''
    Removes specified columns from a DataFrame.
'''
def DeleteColumns(df: pd.DataFrame, columnsToDelete: list) -> pd.DataFrame:
    '''
    Parameters:
        df - DataFrame from which columns will be deleted
        columnsToDelete - List of column names to be removed from the DataFrame

    Returns:
        DataFrame with the specified columns removed
    '''
    df = df.drop(columns=columnsToDelete, errors='ignore')  
    return df


'''
Fills NaN values in a DataFrame. Numeric columns are filled with the column mean,
while string (object) columns are filled with an empty string.
'''
def FillEmptyValues(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Parameters:
        df - DataFrame in which NaN values will be filled

    Returns:
        DataFrame with NaN values replaced as specified
    '''
    for column in df.columns:
        if df[column].dtype in ['float64', 'int64']: 
            mean_value = df[column].mean()  
            df[column] = df[column].fillna(mean_value)  
        elif df[column].dtype == 'object':  
            df[column] = df[column].fillna("")  
    return df

'''
Filters rows in a DataFrame based on a specified condition.
'''
def FilterRows(df: pd.DataFrame, condition: str) -> pd.DataFrame:
    '''
    Parameters:
        df - DataFrame to be filtered
        condition - A string representing the condition to filter rows by,
                    formatted as a query (e.g., "age > 30")

    Returns:
        filtered_df - DataFrame containing rows that meet the specified condition
    '''
    filtered_df = df.query(condition)
    return filtered_df

# Function to select the columns to keep from the DataFrame
def selectColumns(df, columns_to_keep):
    """
    Function to select specific columns from a DataFrame.
    
    :param df: Input DataFrame
    :param columns_to_keep: List of columns to keep
    :return: Transformed DataFrame with only the selected columns
    """
    return df[columns_to_keep]

