from data_processing.extract import CsvExtractor
from helper import ReadJson
from pathlib import Path
from data_processing.transform import (
    DeleteColumns,
    FillEmptyValues,
    FilterRows
    )
from data_processing.load import LoadDfToSqlite

def main():

    #Read Json file to get datasources metadata
    filePath = Path(__file__).parent / r'datasources.json'
    # filePath = r'./datasources.json'
    # print(filePath)
    config = ReadJson(filePath)

    # get DB info
    dbName = Path('../data/TrafficCrashPatterns.db')

    for datasetName, config in config.items():
        #get datesources url
        url = config['url']

        #step-1: Extract data
        df = CsvExtractor(url)

        #Transformation
        #step-2: remove unwanted columns
        transformedDf = DeleteColumns(df,config['columnsToDelete'])

        #step-3: filter dataframe on the bases of filtering query
        if config.get('filteringQuery'):
            transformedDf = FilterRows(transformedDf,config.get('filteringQuery'))

        #step-4: fill empty cells
        transformedDf = FillEmptyValues(transformedDf)

        #step-5: Load it into DB
        LoadDfToSqlite(dbName,datasetName,transformedDf)

if __name__ == "__main__":
    main()