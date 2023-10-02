import click
from utils.upload import upload  
from utils.transform import transform
from utils.query import query

@click.command()
@click.argument('csv_file')
def cli(csv_file):

    upload(csv_file)  
    transform()

if __name__ == '__main__':
    cli()