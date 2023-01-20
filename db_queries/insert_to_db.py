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
    approved_time_id = "2023-01-20 08:01:05"  # Remove
    time_id = st.select_from_time(conn, time)
    time_id = '2023-01-20 09:01:00'  # remove
    location_id = sl.select_from_location(conn, lat, lon)

    val_1 = []
    val_2 = []
    val_3 = []
    val_4 = []
    val_5 = []
    val_6 = []
    val_7 = []
    val_8 = []
    val_9 = []
    val_10 = []
    val_11 = []
    val_12 = []
    val_13 = []
    val_14 = []
    val_15 = []
    val_16 = []
    val_17 = []
    val_18 = []
    val_19 = []

    # LOOP
    counter = 0
    values_string = ""
    for i in range(73):
        for key in data:
            if key == 'approvedTime':
                if data[key] == approved_time_id:
                    val_1 = data[key]
            elif key == 'valid_time':
                val_2 = data[key].split(', ')
                print(len(val_2))
                print(val_2)
                # if val_2[counter] == time_id:
                #     print(data[key][counter])

    category_id = spc.select_from_precipation_category(conn, '1')

    # Location???
    column_string = "approved_time, valid_time, air_pressure, air_temperature, horizontal_visibility, wind_direction, wind_speed, relative_humidity, thunder_probability, mean_value_of_total_cloud_cover, mean_value_of_low_level_cloud_cover, mean_value_of_medium_level_cloud_cover, mean_value_of_high_level_cloud_cover, wind_gust_speed, minimum_precipitation_intensity, maximum_precipitation_intensity, percent_of_precipitation_in_frozen_form, precipitation_category, mean_precipitation_intensity, median_precipitation_intensity, location_id"
    query = f""" INSERT INTO weather.precipitation_category ({column_string}) VALUES {values_string};

({approved_time_id}, '{time_id}, {location_id}, {data['air_pressure'][0]}, {data['air_temperature'][0]}, {data['horizontal_visibility'][0]}, {data['wind_direction'][0]}, {data['wind_speed'][0]}, {data['relative_humidity'][0]}, {data['thunder_probability'][0]}, {data['mean_value_of_total_cloud_cover'][0]}, {data['mean_value_of_low_level_cloud_cover'][0]}, {data['mean_value_of_medium_level_cloud_cover'][0]}, {data['mean_value_of_high_level_cloud_cover'][0]}, {data['wind_gust_speed'][0]}, {data['minimum_precipitation_intensity'][0]}, {data['maximum_precipitation_intensity'][0]}, {data['percent_of_precipitation_in_frozen_form'][0]}, {data['precipitation_category'][0]}, {data['mean_precipitation_intensity'][0]}, {data['median_precipitation_intensity'][0]}),
;
"""

    # try:
    #     # Create a cursor.
    #     cur = conn.cursor()

    #     # Executing statement.
    #     cur.execute(query)
    #     print(f"Values categories added.")

    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error)

    # finally:
    #     # Save table.
    #     conn.commit()

    #     # Close communication with database.
    #     cur.close()

    # conn.close()


if __name__ == '__main__':
    insert_to_db()
