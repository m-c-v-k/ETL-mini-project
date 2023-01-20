#! python3

# Import necessary libraries
import psycopg2


def select_from_approved_time(conn, value):
    query = f"SELECT approved_time_id FROM weather.approved_time WHERE reference_time = '{value}';"
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
