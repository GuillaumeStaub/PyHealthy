from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.constants import Base


class Category(Base):
    """Represents the category table of the database
    with a unique constraint on the name
    Args:
        Base (declarative_base): represents a way to
        interact with the SQLAlchemy ORM
    """

    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True)
    category = relationship("Product", backref='category', lazy="subquery")

    @classmethod
    def select_categories(cls, session):
        """Queries to retrieve all categories included in the database's category table

        Returns:
            database.Categroy: Contains all objects Category in the database
        """
        result = session.query(Category).all()
        return result
