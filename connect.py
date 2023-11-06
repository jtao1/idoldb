from google.cloud.sql.connector import Connector, IPTypes
import pymysql
import os
from dotenv import find_dotenv, load_dotenv
import sqlalchemy

def db_conn():
    dotevn_path = find_dotenv()
    load_dotenv(dotevn_path)
    USER = os.getenv('user')
    PASSWORD = os.getenv('password')
    DB = os.getenv('db')

    connector = Connector()

    def getconn() -> pymysql.connections.Connection:
        conn: pymysql.connections.Connection = connector.connect (
            'cs348-project-403920:us-central1:idol-db',
            'pymysql',
            user=USER,
            password=PASSWORD,
            db=DB,
        )
        return conn

    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )
    return pool.connect()