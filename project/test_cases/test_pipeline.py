

import subprocess
import pytest
import os
import sys
sys.path.append(os.path.abspath('./project'))
from data_processing.transform import (
    selectColumns,
    DeleteColumns,
    FillEmptyValues,
    FilterRows
    )
from data_processing.load import LoadDfToSqlite
import pandas as pd

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))

PIPELINE_SCRIPT_PATH = os.path.abspath("./project/pipeline.py")
OUTPUT_FILE_PATH = os.path.abspath("./data/TrafficCrashPatterns.db")
DATASOURCES_JSON_PATH = os.path.join(PROJECT_ROOT, 'datasources.json')


print("PIPELINE_SCRIPT_PATH", PIPELINE_SCRIPT_PATH)
print("OUTPUT_FILE_PATH", OUTPUT_FILE_PATH)
print("DATASOURCES_JSON_PATH", DATASOURCES_JSON_PATH)

@pytest.fixture
def execute_pipeline():
    # Ensure the output DB file doesn't exist before running the pipeline
    if os.path.exists(OUTPUT_FILE_PATH):
        os.remove(OUTPUT_FILE_PATH)
    
    # Ensure datasources.json is available
    assert os.path.exists(DATASOURCES_JSON_PATH), "datasources.json file not found"
    
    # Run the pipeline script
    subprocess.run(["python", PIPELINE_SCRIPT_PATH], check=True)

@pytest.fixture
def get_sample_data():
    sample_data = {
        'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': [9, 10, 11, 12]
    }
    sample_df = pd.DataFrame(sample_data)
    return sample_df

# Renaming this fixture to avoid the conflict
@pytest.fixture
def get_sample_config_to_delete():
    config = {
        'columnsToDelete': ['B'],
        'filteringQuery': 'C > 10'
    }
    return config

# Renaming this fixture to avoid the conflict
@pytest.fixture
def get_sample_config_to_keep():
    config = {
        'columnsToKeep': ['A', 'C'],  # The columns we want to keep in the DataFrame
    }
    return config

# Test for selectColumns function
def test_select_columns(get_sample_data, get_sample_config_to_keep):
    transformed_df = selectColumns(get_sample_data, get_sample_config_to_keep['columnsToKeep'])
    assert 'A' in transformed_df.columns, "'A' column should be in the transformed DataFrame"
    assert 'C' in transformed_df.columns, "'C' column should be in the transformed DataFrame"
    assert 'B' not in transformed_df.columns, "'B' column should not be in the transformed DataFrame"
    assert transformed_df.shape == (4, 2), f"Expected shape (4, 2), but got {transformed_df.shape}"

# def test_delete_columns(get_sample_data, get_sample_config_to_delete):
#     transformed_df = DeleteColumns(get_sample_data, get_sample_config_to_delete['columnsToDelete'])
#     assert 'B' not in transformed_df.columns, "Column B was not deleted"

# def test_filter_rows(get_sample_data, get_sample_config_to_delete):
#     transformed_df = FilterRows(get_sample_data, get_sample_config_to_delete['filteringQuery'])
#     assert len(transformed_df) == 2, "The dataframe does not contain the expected number of rows"

# def test_fill_empty_values(get_sample_data):
#     transformed_df = FillEmptyValues(get_sample_data)
#     assert not transformed_df.isnull().values.any(), "Not all empty values were filled"

def test_pipeline_output_file(execute_pipeline):
    assert os.path.exists(OUTPUT_FILE_PATH), "Output file was not created by the pipeline."

def test_pipeline_data(execute_pipeline):
    conn = sqlite3.connect(OUTPUT_FILE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert len(tables) > 0, "No tables found in the database"
    cursor.execute("SELECT * FROM TrafficCrashPatterns LIMIT 5;")
    rows = cursor.fetchall()
    assert len(rows) > 0, "No data found in the TrafficCrashPatterns table"
    conn.close()
