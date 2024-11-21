from data_processing.extract import CsvExtractor
from helper import ReadJson
from pathlib import Path
from data_processing.transform import (
    DeleteColumns,
    FillEmptyValues,
    FilterRows
    )
from data_processing.load import LoadDfToSqlite
import os

def main():

    #Read Json file to get datasources metadata
    filePath = Path(__file__).parent / r'datasources.json'
    # filePath = r'./datasources.json'
    # print(filePath)
    config = ReadJson(filePath)
    
    # get DB info and delete the db if a file already exists
    dbName = Path('../data/TrafficCrashPatterns.db')
    if dbName.is_file():
        os.remove(dbName)
        print(f"{dbName} deleted.")

    for datasetName, config in config.items():
        #get datesources url
        url = config['url']

        #step-1: Extract data
        df = CsvExtractor(url)

        #Transformation
        #step-2: remove unwanted columns
        transformedDf = df[config["columnsToKeep"]]
        # print("url", url, "config columns to delete", config['columnsToDelete'], "transformedDf", transformedDf.head())


        #step-3: fill empty cells
        transformedDf =  transformedDf.dropna()
        #step-5: Load it into DB
        LoadDfToSqlite(dbName,datasetName,transformedDf)

if __name__ == "__main__":
    main()