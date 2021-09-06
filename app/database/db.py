# Database connection

'''class ExampleDB:
    def __init__(self, db):
        self.db = db

    def connect(self):
        pass'''


# connection to db
from sqlalchemy import create_engine
from app.utils.config import config_by_name
from sqlalchemy.orm import sessionmaker, scoped_session

config = config_by_name['BasicConfig']

DATABASE_URL = f'postgresql://{config.db_user}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_database}'

print(DATABASE_URL)

engine = create_engine(DATABASE_URL)

Session = scoped_session(sessionmaker(bind=engine))