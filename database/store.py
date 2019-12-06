from sqlalchemy import Column, Integer, String
from config.constants import Base


class Store(Base):
    """Represents the store table of the database
    with a unique constraint on the name
    Args:
        Base (declarative_base): represents a way to interact
        with the SQLAlchemy ORM
    """

    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    