""" Query the top 5 rows from nomorePandas.db """
import sqlite3
import os
import glob


def query(db="nomorePandas.db"):
    """
    param: db: str
    return: top 5 rows of the table
    """
    dataset_files = glob.glob("datasets/*.csv")
    if not dataset_files:
        print("No CSV files found in the 'datasets' folder.")
        return

    latest_dataset = max(dataset_files, key=os.path.getctime)
    table_name = os.path.splitext(os.path.basename(latest_dataset))[0]

    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 3")

    print(f"Top 5 rows of the {table_name} table:")
    column_names = [i[0] for i in cursor.description]
    print("\t".join(column_names))

    for row in cursor.fetchall():
        print("\t".join(str(value) for value in row))

    conn.close()
    return "Done"


# if __name__ == "__main__":
#     query()
