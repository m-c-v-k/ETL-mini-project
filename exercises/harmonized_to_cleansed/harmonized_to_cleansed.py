#! python3

# Import necessary libraries
import os
import json
import psycopg2
import re


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
open_path = f'{CURR_DIR_PATH}/../data/testing/harmonized'
save_path = f'{CURR_DIR_PATH}/../data/testing/cleansed'


def read_data():

    f = open(f'{open_path}/data.txt', 'r')
    data = f.readline()
    f.close()

    f = open(f'{open_path}/data_keys.txt', 'r')
    data_keys = f.readline()
    f.close()

    return data, data_keys


def connect_to_db():
    conn = None

    try:
        print("Connecting to database...")
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="archprep",
            user="postgres",
            password="MisoDaisy"
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return conn


def insert_to_db():
    data, keys = read_data()

    data = json.loads(data)

    value_list = []
    for item in data:
        value_list.append(item[1])

    value_string = ""
    for item in value_list:
        if type(item) == list:
            item = str(item)
        if re.search("'", item):
            item = item.replace("'", '')
        if re.search("\[", item):
            item = item.replace("[", '')
        if re.search("\]", item):
            item = item.replace("]", '')
        value_string += f"'{item}', "

    value_string = value_string[:-2]
    keys = keys[1:-1]
    name = value_list[0]

    conn = connect_to_db()

    try:
        cur = conn.cursor()

        cur.execute(f"""INSERT INTO cleansed.people ({keys})
VALUES ({value_string});""")
        print(f"{name} added.")

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    conn.close()


insert_to_db()
