#! python3

# Import necessary libraries
import os
import pandas as pd
import requests
import json


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
save_path = f'{CURR_DIR_PATH}/../data/testing/raw'


def get_endpoint():
    # TODO get user position - Depending on Time
    # TODO Chose position

    # Example test variables
    lon = "16.158"
    lat = "58.5812"

    # TODO single-point/multi-point? - Depending on time Multipoint as well
    set_type = 'point'

    # TODO Check within bounds - Fix at a later time

    # TODO if out-of-bounds, error message and default location -> Stockholm - Start / Easter egg - If time

    url_protocol = "https"
    url_domain = "opendata-download-metfcst.smhi.se"
    url_API = "api/category/pmp3g/version/2"
    url_type = f"geotype/{set_type}"
    url_point = f"lon/{lon}/lat/{lat}"
    url_data = "data.json"
    URL = f"{url_protocol}://{url_domain}/{url_API}/{url_type}/{url_point}/{url_data}"

    return URL


def get_raw_data():

    URL = get_endpoint()

    r = requests.get(URL)

    return r


def save_dict_to_json():
    data = get_raw_data()

    df = pd.DataFrame(data)

    df.to_json(f'{save_path}/data.json')


save_dict_to_json()
