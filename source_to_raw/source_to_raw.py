#! python3

# Import necessary libraries
import os
import datetime
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


def get_time(approved_time):
    approved_time = datetime.datetime.strptime(
        approved_time, '%Y-%M-%dT%H:%S:%fZ')
    approved_time = datetime.datetime.strftime(
        approved_time, '%Y-%M-%d_%H')

    return approved_time


def save_to_json():
    data = get_raw_data()
    data = json.loads(data.text)

    approved_time = get_time(data['approvedTime'])

    with open(f'{save_path}/raw_data_{approved_time}.json', 'w+') as f:
        json.dump(data, f, indent=3)


if __name__ == '__main__':
    save_to_json()
