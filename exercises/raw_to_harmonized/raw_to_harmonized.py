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

    keys = []

    for value in data:
        keys.append(value[0])

    return data, keys


def harmonize_data():
    data, keys = read_data()
    df = pd.DataFrame(data)

    with open(f'{save_path}/data.txt', 'w+') as f:
        json.dump(data, f)

    with open(f'{save_path}/data_keys.txt', 'w+') as f:
        json.dump(keys, f)


harmonize_data()
