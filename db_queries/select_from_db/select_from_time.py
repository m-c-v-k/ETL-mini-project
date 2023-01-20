#! python3

# Import necessary libraries
import psycopg2


def select_from_time(conn, time):
    query = f"""SELECT time_id FROM weather.time 
WHERE year = '{time[:4]}' 
AND month = '{time[5:7]}' 
AND day = '{time[8:10]}' 
AND hour = '{time[11:13]}' 
AND minute = '{time[14:16]}' 
AND second = '{time[17:20]}';"""
    value_id = ""

    try:
        # Create a cursor.
        cur = conn.cursor()

        # Executing a statement.
        cur.execute(query)

        # Check return from executed statement.
        rows = cur.fetchall()

        if rows == []:
            print("It seems as if there is no matching time.")
        else:
            for row in rows:
                print("Time found.")
                print(row)
                value_id = row

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:

        cur.close()

        if value_id == "":
            value_id = None
        return value_id
