from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.constants import Base, store_product
from database.category import Category
from database.store import Store


class Product(Base):
    """Represents the product table of the database with a ForeignKEy
    to connect a product to a category

    Args:
        Base (declarative_base): represents a way
        to interact with the SQLAlchemy ORM
    """
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    nutriscore = Column(String(1))
    url = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    stores = relationship("Store", secondary=store_product, backref='product')

    @classmethod
    def select_products(cls, session, categroy):
        """Query that retrieves all products whose nutriscore is greater than "B"

        Args:
            session (session): allow to send requests to the database
            categroy (int): category is an integer that matches the id of
            the category whose products are to be retrieved.

        Returns:
            Products: Database Products objects
        """
        result = session.query(Product)\
                        .filter(Product.category_id == categroy)\
                        .filter(Product.nutriscore > "b")\
                        .join(Category).order_by(func.rand()).limit(10).all()
        return result

    @classmethod
    def find_healthy(cls, session, fat_product, category):
        """Queries that retrieves a healthier product
        than the product selected by the user

        Args:
            session (session): allow to send requests to the database
            product_s (Products): Database Product object
            category (int): category is an integer that matches the id of
            the category whose products are to be retrieved.

        Returns:
            Products: Database Product object
        """
        result = session.query(Product)\
                        .filter(Product.category_id == category)\
                        .filter(Product.nutriscore < fat_product.nutriscore)\
                        .limit(1).first()
        return result

    @classmethod
    def load_product(cls, product_id, session):
        """Query that loads the product corresponding to the id of the desired product.

        Args:
            product_id (int): product id research
            session (session): allow to send requests to the database

        Returns:
            Product: Database Product object
        """
        result = session.query(Product)\
                        .filter(Product.id == product_id).first()
        session.refresh(result)
        return result

    def __repr__(self):
        """Represents how the product objects are displayed
        """
        return(f"\033[94m Nom du produit:\033[0m {self.name.capitalize()}"
               f"\033[94m Catégorie:\033[0m {self.category.name.capitalize()}"
               f"\033[94m Nutriscore:\033[0m {self.nutriscore.upper()}")

    @property
    def format_stores(self):
        return ", ".join([x.name.capitalize() for x in self.stores])


if __name__ == "__main__":
    pass
