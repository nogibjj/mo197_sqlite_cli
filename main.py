# import click
from utils.extract import copy_latest_csv_to_datasets
from utils.transform_load import load
from utils.query import query
import fire


class ETLCommands:
    def etl(self):
        """Extract, tranform and load data to db."""
        print("Extracting data...")
        copy_latest_csv_to_datasets()
        print("Transforming data...")
        load()

    def query(self):
        """Query data."""
        print("Querying data...")
        query()


if __name__ == "__main__":
    fire.Fire(ETLCommands)
