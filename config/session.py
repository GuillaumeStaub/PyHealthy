from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


class Session():
    """This class was created to prevent more than one session
    from being opened in the program at the same time.
    It also allows you to recycle code that is used
    a few times in the program.

    Returns:
        session: Returns a session that acts as an intermediary
        between python and the database.
    """

    def __init__(self):
        """Initializes the session with engine that retrieves
        database connection items
        """
        self.engine = create_engine(os.getenv("DATABASE_URL"))

    @property
    def session(self):
        """Set up the session and return a Session object.

        Returns:
            session: Returns a session that acts as an intermediary
            between python and the database.
        """
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
