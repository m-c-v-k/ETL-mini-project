#! python3

# Import necessary libraries
import os
import glob
import datetime
import json
import psycopg2
from connect_to_db import connect_to_db as connect
from select_from_db import select_from_approved_time as sat
from select_from_db import select_from_precipation_category as spc
from select_from_db import select_from_location as sl
from select_from_db import select_from_time as st


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OPEN_PATH = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def get_harmonized_data():
    os.chdir(OPEN_PATH)
    files_list = glob.glob('*.txt')
    data_file = max(files_list, key=os.path.getctime)

    with open(f'{OPEN_PATH}/{data_file}', 'r') as f:
        data = json.load(f)

    return data


def insert_to_db():
    data = get_harmonized_data()
    conn = connect.connect_to_db()

    # TODO change values to variables
    lat = 18
    lon = 16
    time = "2023-01-19 15:01:05"
    approved_time_id = sat.select_from_approved_time(conn, '1')
    category_id = spc.select_from_precipation_category(conn, '1')
    location_id = sl.select_from_location(conn, lat, lon)
    time_id = st.select_from_time(conn, time)
    print(time_id)

    """ INSERT INTO weather (list_of_columns)
    VALUES 
    (String 1),
    (string 2)
    """

    conn.close()


if __name__ == '__main__':
    insert_to_db()
