import os
import sqlite3
import pandas as pd

UPLOAD_DIR = 'uploads'

def transform():

    # Get latest CSV file
    latest_csv = get_latest_csv()
    
    # Read CSV into dataframe 
    df = pd.read_csv(latest_csv)

    # Transform dataframe
    df = transform_dataframe(df)

    # Load into SQLite DB
    load_to_sqlite(latest_csv, df)
    
    print('Transformed latest CSV')

def get_latest_csv():
    # Logic to get latest CSV file
    return latest_csv 

def transform_dataframe(df):
    # Transform logic
    return df

def load_to_sqlite(csv_path, df):
    # Logic to load to SQLite DB