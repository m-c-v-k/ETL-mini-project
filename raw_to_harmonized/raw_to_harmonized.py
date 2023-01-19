#! python3

# Import necessary libraries
import os
import glob
import pandas as pd
import json

# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OPEN_PATH = f'{CURR_DIR_PATH}/../data/testing/raw'
SAVE_PATH = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def get_raw_Data():

    os.chdir(OPEN_PATH)
    files_list = glob.glob('*.json')
    data_file = max(files_list, key=os.path.getctime)

    with open(f'{OPEN_PATH}/{data_file}', 'r') as f:
        data = json.load(f)

    return data, data_file


def harmonize_data():
    data, file_name = get_raw_Data()

    with open(f'{SAVE_PATH}/data.txt', 'w+') as f:
        json.dump(data, f)


harmonize_data()
