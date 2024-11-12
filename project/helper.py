import json


'''
Read Json file
'''

def ReadJson(filePath:str)->str:
    '''
    Parameters:
        filePath - Path to the json file

    Returns:
        configDate - string readed from json file 
    '''
    with open(filePath, 'r') as file:
        configData = json.load(file) 
    
    return configData