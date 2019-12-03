from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import  relationship
from config.constants import Base, store_product

class Favorites(Base):
    """Represents the favorites table of the database.
    This table points directly to the product table,
    to recover the substituted product and the substitute.
    Args:
        Base (declarative_base): represents a way to interact with the SQLAlchemy ORM
    """

    __tablename__='favorites'

    id = Column(Integer, primary_key=True)
    product_substituted = Column(String(100))
    products_substitue =  Column(String(100))
