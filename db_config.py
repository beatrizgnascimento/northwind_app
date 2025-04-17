import psycopg2
import sqlalchemy

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="northwind",
        user="postgres",
        password="postgres"
    )
def get_engine():
    return sqlalchemy.create_engine("postgresql+psycopg2://postgres:postgres@localhost/northwind")