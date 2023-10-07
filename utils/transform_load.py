import sqlite3

# import csv
import os
import pandas as pd

# import re
from glob import glob


def load():
    dataset_files = glob("datasets/*.csv")
    if not dataset_files:
        print("No CSV files found in the 'datasets' folder.")
        return

    latest_dataset = max(dataset_files, key=os.path.getctime)

    df = pd.read_csv(latest_dataset)

    df.dropna(axis=1, how="all", inplace=True)

    df.columns = df.columns.str.replace("[^a-zA-Z]", "", regex=True)

    df.columns = df.columns.str.lower().str.replace(" ", "_")

    conn = sqlite3.connect("nomorePandas.db")
    cursor = conn.cursor()

    table_name = os.path.splitext(os.path.basename(latest_dataset))[0]
    create_table_query = (
        f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(df.columns)})"
    )
    cursor.execute(create_table_query)
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    print("Sucessfully dumped the dataset to the DB")


# if __name__ == "__main__":
#     load()
