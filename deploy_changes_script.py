import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'pass',
    'database': 'database'
}

SQL_CHANGES = [
]

def Dep_change():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        print("Connected to the database.")

        for change in SQL_CHANGES:
            try:
                print(f"Executing:\n{change.strip()}")
                cursor.execute(change)
                print("Change applied.")
            except Error as err:
                print(f"Failed to apply change:\n{err}")

        connection.commit()
        print("Changes Commited")

    except Error as e:
        print(f"Error encounter in SQL: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    Dep_change()
