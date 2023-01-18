#! python3

# Import necessary libraries
import os
import json
# import psycopg2
import pandas as pd
import re


# Set paths
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
open_path = f'{CURR_DIR_PATH}/../data/testing/harmonized'
save_path = f'{CURR_DIR_PATH}/../data/testing/cleansed'


def read_data():

    f = open(f'{open_path}/data.txt', 'r')
    data = f.readline()
    f.close()

    return data


def cleanse_data():
    data = read_data()
    data = data.replace('\\', '')
    data = data[3:-1]

    data_list = data.split('","')

    new_data = ""
    for item in data_list:
        if re.search(
                '''\[\d{1,2}(,\d{1,2})?.\d{1,6}"\]|\["\d{1,2}(,\d{1,2})?.\d{1,6}\]''', item):
            if ':' in item:
                split_item = item.split(":")
                split_item[1] = split_item[1].replace('"', '')
                item = (':').join(split_item)
            else:
                item = item.replace('"', '')

        new_data += f"{item},"

    with open(f'{save_path}/data.txt', 'w+') as f:
        f.write(new_data)

    data = json.loads(new_data)

    value_list = []
    for item in data:
        print(item)
        value_list.append(item)

    # new_data = new_data.replace('"', "'")

    # value_string = ""
    # for item in value_list:
    #     if type(item) == list:
    #         item = str(item)
    #     if re.search("'", item):
    #         item = item.replace("'", '')
    #     if re.search("\[", item):
    #         item = item.replace("[", '')
    #     if re.search("\]", item):
    #         item = item.replace("]", '')
    #     value_string += f"'{item}', "

    # value_string = value_string[:-2]
    # keys = keys[1:-1]
    # name = value_list[0]

    # print(value_string)
    # print(keys)
    # print(name)


#     conn = connect_to_db()

#     try:
#         cur = conn.cursor()

#         cur.execute(f"""INSERT INTO cleansed.people ({keys})
# VALUES ({value_string});""")
#         print(f"{name} added.")

#         conn.commit()
#         cur.close()

#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     conn.close()

cleanse_data()
