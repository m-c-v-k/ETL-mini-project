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

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing statement.
        cur.execute(f""" INSERT INTO weather.precipitation_category (category_id, meaning)
VALUES 
({data[0][0]}, '{data[0][1]}'),
({data[1][0]}, '{data[1][1]}'),
({data[2][0]}, '{data[2][1]}'),
({data[3][0]}, '{data[3][1]}'),
({data[4][0]}, '{data[4][1]}'),
({data[5][0]}, '{data[5][1]}'),
({data[6][0]}, '{data[6][1]}');
""")
        print(f"Precipation categories added.")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        # Save table.
        conn.commit()

        # Close communication with database.
        cur.close()

    conn.close()


if __name__ == '__main__':
    insert_data_to_precipation_category()
