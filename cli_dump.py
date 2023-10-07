# import click
from utils.extract import copy_latest_csv_to_datasets
from utils.transform_load import load

if __name__ == "__main__":
    copy_latest_csv_to_datasets()
    load()
