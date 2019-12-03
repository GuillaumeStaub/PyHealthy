from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config.constants import store_product
import os

class Session():

    @staticmethod
    def session():
        engine = create_engine(os.getenv("DATABASE_URL"))
        engine.connect()
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        return session