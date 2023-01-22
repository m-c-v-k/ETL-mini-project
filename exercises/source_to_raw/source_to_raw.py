#! python3

# Import necessary libraries
import os
import pandas as pd
import requests
import json


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
save_path = f'{CURR_DIR_PATH}/../data/testing/raw'


def get_raw_data():
    r = requests.get('https://swapi.dev/api/people/1/')

    return r


def save_dict_to_json():
    data = get_raw_data()
    data = data.json()

    df = pd.DataFrame(data.items())

    df.to_json(f'{save_path}/data.json')


save_dict_to_json()
