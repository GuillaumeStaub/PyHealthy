import os
import time
import logging
import requests
import json

from sqlalchemy import create_engine, inspect, Column, Integer, String, ForeignKey, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
from sqlalchemy.exc import ProgrammingError

from install.product_downloader import ProductDownloader
from install.product_cleaner import ProductCleaner
from database.category import Category
from database.product import Product
from database.store import Store
from database.favorites import Favorites
from install.progress_bar import ProgressBar
from config.constants import search_terms, Base, read_log


class Install():
    """Class that initializes the classes responsible for downloading data,
    cleaning them, creating the database and saving data to the database.

    """

    def __init__(self, size):
        """Initializes all tool classes, and config data for the database
        """
        self.download_datas = [
            ProductDownloader(
                term,
                page_size=size).recover_product for term in search_terms]
        self.clean_datas = ProductCleaner(self.download_datas).clean_products
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.connect = self.engine.connect()
        self.session = self.session_method()
        self.categories = {}
        self.stores = {}

    def create_bdd(self):
        """Drop and Create all tables in our database if they are not already present
        """
        Base.metadata.drop_all(self.engine, checkfirst=True)
        Base.metadata.create_all(self.engine, checkfirst=True)

    def session_method(self):
        """The SQLAlchemy session is used to communicate with the database and serves as a storage area for all objects related to the database

        Returns:
            Session: allows communication with the database
        """
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()
        return session

    def generate_category(self, datas):
        """Retrieves a category from the cleaned data and integrates it into the database.
        The method checks if the category is not already in the database thanks to an intermediate
        python dict that links the name of the category and its id in the database.

        Args:
            datas (dict): clean datas dictionnary

        Returns:
            str: This return makes it possible to query the intermediate dictionary
             and to insert the id of the category to the product.
        """
        category = datas["categories"]
        if category not in self.categories:
            new_cat = Category(name=category)
            self.session.add(new_cat)
            self.session.commit()
            self.categories[category] = new_cat.id
        return category

    def generate_stores(self, product, datas):
        """Allows you to retrieve a list of input stores, to distribute these stores
        in the warehouse table while linking the product to the stores thanks
        to an intermediate table.

        Args:
            product (instance): Product instance for stores related
            datas (dict) : clean datas dictionnary
        """
        stores = datas["stores"]
        for store in stores:
            if store not in self.stores:
                new_store = Store(name=store)
                self.session.add(new_store)
                self.stores[store] = new_store
            else:
                new_store = self.stores[store]
            product.stores.append(new_store)

    def load_datas_db(self):
        """This method provides access to clean data from the API, and methodically loads it into the database
        """
        for data in self.clean_datas:
            category = self.generate_category(data)
            product = Product(
                name=data["name"],
                nutriscore=data["nutriscore"],
                url=data["url"],
                category_id=self.categories[category])
            self.generate_stores(product, data)
            self.session.add(product)
            self.session.commit()


def main(count):
    try:
        p = ProgressBar(count)
        p.start()
        i = Install(count)
        i.create_bdd()
        i.load_datas_db()
    except requests.exceptions.SSLError:
        p.kill()
        logging.critical("There is a problem with the OFF servor")
    except requests.exceptions.ConnectionError:
        p.kill()
        logging.critical('There is no internet connection')
    except json.decoder.JSONDecodeError:
        p.kill()
        logging.critical(
            'There is a problem with datas. Verify the link in config.constants')
    except ProgrammingError as e:
        p.kill()
        logging.critical(e)
    finally:
        read_log()


if __name__ == "__main__":
    pass
