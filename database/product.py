from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import  relationship
from sqlalchemy.sql import func
from config.constants import Base, store_product
from config.session import Session
from database.store import Store
from database.category import Category

class Product(Base):
    """Represents the product table of the database with a ForeignKEy 
    to connect a product to a category
    
    Args:
        Base (declarative_base): represents a way to interact with the SQLAlchemy ORM
    """
    __tablename__='product'

    id = Column (Integer, primary_key = True)
    name = Column (String(150))
    nutriscore = Column(String(1))
    url = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    stores = relationship("Store", secondary = store_product, backref='product')


    @classmethod
    def select_all(cls, categroy):
        session = Session.session()
        result = session.query(Product).filter(Product.category_id==categroy).filter(Product.nutriscore > "b").join(Category).order_by(func.rand()).limit(10).all()
        return result
    
    @classmethod
    def find_healthy(cls, product_s, category):
        session = Session.session()
        result = session.query(Product).filter(Product.category_id == category).filter(Product.nutriscore < product_s.nutriscore).limit(1).all()
        return result
if __name__ == "__main__":
    pass
