import os
from sqlalchemy.orm import sessionmaker, declarative_base
import sqlalchemy as sq
from dotenv import load_dotenv
from pprint import pprint
from req import get_request
from models import Tasks

load_dotenv()

Base = declarative_base()


data_api = get_request(os.getenv('API_URL'))
DSN = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}"
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

def create_tables(engine):
    Base.metadata.create_all(engine)

def drop_tables(engine):
    Base.metadata.drop_all(engine)

def update_db(data_api):
    data_db = (session.query(Tasks.id).all())
    data_id = list([i[0] for i in data_db])
    for i in data_api:
        data_table = Tasks(**i)
        if data_table.id in data_id:
            pass
        else:
            session.add(data_table)
    print('БД успешно обновлена!')

def get_db():
    pprint(session.query(Tasks).all())




if __name__ == '__main__':
    data_api = get_request(os.getenv('API_URL'))

    DSN = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@localhost:5432/{os.getenv('DB_NAME')}"
    engine = sq.create_engine(DSN)

    Session = sessionmaker(bind=engine)
    session = Session()
    update_db(data_api)
    get_db()

    session.commit()
    session.close()
