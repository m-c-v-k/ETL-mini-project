#! python3

# Import necessary libraries
import os
import pandas as pd
import json

# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
open_path = f'{CURR_DIR_PATH}/../data/testing/raw'
save_path = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def read_data():

    data = pd.read_json(f'{open_path}/data.json')
    data = list(data.itertuples(index=False, name=None))

    return data


def harmonize_data():
    data = read_data()

    with open(f'{save_path}/data.txt', 'w+') as f:
        json.dump(data, f)


harmonize_data()
