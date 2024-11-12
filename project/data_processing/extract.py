import pandas as pd
from io import StringIO
import requests


'''
To extract csv data from the provided url
'''
def CsvExtractor(csvUrl: str) -> pd.DataFrame:
    '''
    Parameters:
        csvUrl - URL to the CSV file

    Returns:
        df - DataFrame containing the CSV data read from the provided URL
    '''
        
    response = requests.get(csvUrl)
    response.raise_for_status()

    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data,low_memory=False)

    return df
