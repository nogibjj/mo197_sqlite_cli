import sqlite3 
import pandas as pd
import click

@click.command()
@click.argument('db_name')
@click.argument('sql_query')
def query(db_name, sql_query):

    conn = sqlite3.connect(f'{db_name}.db')
    
    print(pd.read_sql(sql_query, conn))