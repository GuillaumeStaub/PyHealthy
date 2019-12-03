from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import  relationship
from config.constants import Base
from config.session import Session
import os 


class Category(Base):
    """Represents the category table of the database
    with a unique constraint on the name
    Args:
        Base (declarative_base): represents a way to interact with the SQLAlchemy ORM
    """

    __tablename__='category'

    id = Column (Integer, primary_key = True)
    name = Column (String(40), unique=True)
    category = relationship("Product", backref = 'category')

   
    @classmethod
    def select_all(cls):
        session = Session.session()
        result = session.query(Category).all()
        return result