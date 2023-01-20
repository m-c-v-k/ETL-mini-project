#! python3

# Import necessary libraries
import os
import psycopg2
from connect_to_db import connect_to_db as connect


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
OPEN_PATH = f'{CURR_DIR_PATH}/../data/testing/harmonized'


def insert_data_to_precipation_category():
    conn = connect.connect_to_db()

    data = [
        ["0", "No precipitation"],
        ["1", "Snow"],
        ["2", "Snow and rain"],
        ["3", "Rain"],
        ["4", "Drizzle"],
        ["5", "Freezing rain"],
        ["6", "Freezing drizzle"]
    ]

    print(data[0])
    print(data[0][0])

    """ INSERT INTO weather.precipitation_category (list_of_columns)
    VALUES 
    (String 1),
    (string 2)
    """

    conn.close()


if __name__ == '__main__':
    insert_data_to_precipation_category()
