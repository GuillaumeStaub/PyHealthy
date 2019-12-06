from sqlalchemy import Column, Integer, ForeignKey
from config.constants import Base


class Favorites(Base):
    """Represents the favorites table of the database.
    This table points directly to the product table,
    to recover the substituted product and the substitute.
    Args:
        Base (declarative_base): represents a way to interact
        with the SQLAlchemy ORM
    """

    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True)
    fat_product = Column(Integer, ForeignKey('product.id'), nullable=False)
    healthy_product = Column(Integer, ForeignKey('product.id'), nullable=False)

    @classmethod
    def select_favorites(cls, session):
        """Method to retrieve all Favorites from the Database Favorites table

        Returns:
            database.Favorites: Contains all the favorite
            objects in the database
        """
        result = session.query(Favorites).all()
        return result
