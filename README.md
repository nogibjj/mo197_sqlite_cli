# mo197_sqlite_cli
A simple CLI tool for SQLite database loading, transformation and loading 

This repository provides a CLI for uploading, transforming, and querying CSV files into a SQLite database.

### Usage
#### Upload CSV
The `utils/upload.py` script uploads a CSV file from your local machine to the uploads folder in the current working directory. If the uploads folder does not exist, it will be created.

This will copy the CSV file into the uploads folder.

#### Transform CSV
Once a CSV file is uploaded, the transform.py script will automatically:

Load the latest CSV file from the uploads folder
Transform the data by removing all NULL columns, converting column names to uppercase, and removing spaces
Load the data into a SQLite database named after the CSV file
If the database already exists, only insert new rows rather than the entire data
This happens automatically every time a new CSV file is uploaded.

#### Query Database
`utils/query.py` script allows interacting with the SQLite database created from an uploaded CSV file.
This will connect to the database <db_name>.db and execute the SQL query provided.

```python
python cli.py query <db_name> "<sql_query>"
```