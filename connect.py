from google.cloud.sql.connector import Connector
import pymysql
import os
from dotenv import find_dotenv, load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

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

    engine = create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session()



Base = declarative_base()

class Idols(Base):
    __tablename__ = 'idols'

    idol_id = Column(Integer, primary_key=True)
    birthdate = Column(Date)
    company = Column(String(255))
    country = Column(String(255))
    gender = Column(String(255))
    group_ = Column(String(255))
    height_cm = Column(Integer)
    name = Column(String(255))
    stage_name = Column(String(255))

class Groups(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True)
    code = Column(String(255))
    company = Column(String(255))
    member_count = Column(Integer)
    name = Column(String(255))

class Company(Base):
    __tablename__ = 'company'

    company_id = Column(Integer, primary_key=True)
    company_name = Column(String(255))
    group_count = Column(Integer)
    idol_count = Column(Integer)