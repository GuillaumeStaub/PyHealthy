import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey
'''
 Contains all  constants, parameters of the program
'''
# Link requested to OpenFoodFact API
api_url_OPFF = 'https://fr.openfoodfacts.org/cgi/search.pl'

# Number of product requested by category
size_search = 100

# Categories requested
search_terms = ["pizza", "biscuit", "chips", "sauce", "soda"]

Base = declarative_base()

# Intermediate table between products and stores
store_product = Table('store_product', Base.metadata,
                      Column('product_id', Integer, ForeignKey('product.id')),
                      Column('store_id', Integer, ForeignKey('store.id'))
                      )

# Setup Logger
logging.basicConfig(
    filename='install/myapp.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    datefmt="%d/%m/%Y %I:%M:%S %p")


# Read file logger when python raise an exception
def read_log():
    lines = [ligne.split(' :: ')
             for ligne in open('install/myapp.log') if '::' in ligne]
    [print(date, lvl, msg)
     for date, lvl, msg in lines if lvl in ('ERROR', 'CRITICAL')]


# colors print
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
