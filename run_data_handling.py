#! python3

# Importing necessary libraries
from source_to_raw import source_to_raw as s2r
from raw_to_harmonized import raw_to_harmonized as r2h
from db_queries import insert_to_db as i2db

if __name__ == '__main__':
    s2r.save_raw_data(12.806510, 55.380277)
    r2h.save_harmonized_data()
    i2db.insert_to_db()

    s2r.save_raw_data(17.818135, 66.051505)
    r2h.save_harmonized_data()
    i2db.insert_to_db()

    s2r.save_raw_data(20.259427, 67.846472)
    r2h.save_harmonized_data()
    i2db.insert_to_db()

    s2r.save_raw_data(23.403894, 67.192785)
    r2h.save_harmonized_data()
    i2db.insert_to_db()

    s2r.save_raw_data(14.501744, 63.200153)
    r2h.save_harmonized_data()
    i2db.insert_to_db()
