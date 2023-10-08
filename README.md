# mo197_sqlite_cli
A simple CLI tool for SQLite database loading, transformation and loading 

This repository provides a CLI for uploading, transforming, and querying CSV files into a SQLite database.

### Scripts
The `utils/extract.py` 
Copies the most recent CSV file located in the "Downloads" folder to the "datasets" folder of the current working directory.
Usage Instructions:
- If the "datasets" folder does not exist, follow these steps:
- If you see this message: "The 'datasets' folder does not exist. Please navigate to the root directory of the clone repository," it means you are not in the root directory of the clone repository. In that case, navigate to the root of the clone repository and run the script again.

The `utils/transform_load.py` 
- Loads the most recent CSV file located in the "datasets" folder of the cloned repository.
- Performs data transformations on the loaded CSV file.
- Connects to an SQLite database and creates a table.
- Dumps the transformed data into the database.
Data Transformations:
- Removes columns with 100% null values.
- Converts column names to lowercase and replaces spaces with underscores.
- Database Connection:Connects to the nomorePandas.db SQLite database in the root directory of the cloned repository. If the database does not exist, it is created.
- Table Creation: Creates a table in the database with a name matching the CSV file name (without the extension) and includes the column names after transformation.

### Usage

Run the script as follows:
To perform ETL (Extract, Transform, Load) process:
```python
python main.py etl
```
To perform data querying:
```python
python main.py query
```

Example of the output: