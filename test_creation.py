import sqlite3


def list_table_info():
    # Connect to the SQLite database
    conn = sqlite3.connect("nomorePandas.db")
    cursor = conn.cursor()

    # Get a list of table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    if not tables:
        print("No tables found in the database.")
    else:
        for table in tables:
            table_name = table[0]
            print(f"Table: {table_name}")

            # Get the columns in the table
            # https://stackoverflow.com/questions/22505494/
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()

            print("Columns:")
            for column in columns:
                print(column[1])

    # Close the database connection
    conn.close()

    # ********* prints this out ***********
    # ****** TODO - Make this a py test
    # Table: Electric_Vehicle_Population_Data
    # Columns:
    # vin
    # county
    # city
    # state
    # postalcode
    # modelyear
    # make
    # model
    # electricvehicletype
    # cleanalternativefuelvehiclecafveligibility
    # electricrange
    # basemsrp
    # legislativedistrict
    # dolvehicleid
    # vehiclelocation
    # electricutil


if __name__ == "__main__":
    list_table_info()
