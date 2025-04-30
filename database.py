import urllib
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

class Database():

    def __init__(self):

        self.server = os.getenv('Server')
        self.driver = os.getenv('Driver')
        self.database_name = os.getenv('DataBaseBronze')
        self.user = os.getenv('user') 
        self.password = os.getenv('Password')
        self.engine = self.create_connection()
        self.SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=self.engine)

    def create_connection(self):
        params = urllib.parse.quote_plus(
            f'DRIVER={{{self.driver}}};'
            f'SERVER={self.server};'
            f'DATABASE={self.database_name};'
            f'UID={self.user};'
            f'PWD={self.password};'
            'Encrypt=yes;'
            'TrustServerCertificate=yes;'
        )
        return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
       
database = Database()
engine = database.engine
SessionLocal = database.SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

