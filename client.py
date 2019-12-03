from __future__ import unicode_literals,print_function
from pyfiglet import Figlet
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.category import Category
from database.product import Product
from database.store import Store
from config.constants import Base, store_product


from PyInquirer import prompt, Separator, style_from_dict
import sys, os
class Client():

    def __init__(self):
        f = Figlet(font='slant')
        print (f.renderText('Welcome on PyHealthy'))
        self.answer_home = None
        self.answer_category = None
        self.answer_product = None
        self.dict_category = {}
        self.product = []
        self.dict_product = None
        self.subsitue_answer = None
       


    def home(self):
        print("Bienvenue sur PyHealthy, l'application qui a pour but de mettre un peu plus de sains dans votre vie.")
        print ("Page d'accueil :")
        print ("A tout moment dans le programme faites [q] pour quitter")
        print("Que souhaitez vous faire ? ")
        print("1. Voulez vous substitué un produit ? ")
        print("2. Voulez-vous accéder à vos aliments déjà substitués ?")
        while True : 
            if self.answer_home in ["q", "Q"]:
                sys.exit()
            self.answer_home = input("Votre choix : ")
            try : 
                self.answer_home = int(self.answer_home)
                assert self.answer_home > 0 and self.answer_home <= 2
                break
            except AssertionError:
                print("Saisissez une chiffre entre 1 et 2.")
            except ValueError:
                print("Saisissez un chiffre entre 1 et 2 non une lettre.")
        return self.answer_home

    def category_choice(self):
        print("Choisissez une catégories parmi les suivantes :")
        result = Category()
        self.dict_category = {row.id : row.name for row in result.select_all()}
        [print(f"{x}. {y.capitalize()}") for x, y in sorted(self.dict_category.items())]
        while True : 
            if self.answer_category in ["q", "Q"]:
                sys.exit()
            self.answer_category = input("Votre choix : ")
            try : 
                self.answer_category = int(self.answer_category)
                assert self.answer_category > 0 and self.answer_category <= len(self.dict_category)
                break
            except AssertionError:
                print(f"Saisissez une chiffre entre 1 et {len(self.dict_category)}.")
            except ValueError:
                print(f"Saisissez un chiffre entre 1 et {len(self.dict_category)} non une lettre.")
        return self.answer_category


    def product_choice(self):
        print("*************************************")
        print("Choisissez un produit a substitué :")
        print("*************************************")
        p = Product()
        i = 1
        for row in p.select_all(self.answer_category):
            self.product.append({"choice":i,"product":row})
            print(f"\033[95m{i}.\033[0m \033[94m Nom du produit:\033[0m {row.name.capitalize()} \033[94m Catégorie:\033[0m {row.category.name.capitalize()} \033[94m Nutriscore:\033[0m {row.nutriscore}")
            i+=1
        while True : 
            if self.answer_product in ["q", "Q"]:
                sys.exit()
            self.answer_product = input("Votre choix : ")
            try : 
                self.answer_product = int(self.answer_product)
                assert self.answer_product > 0 and self.answer_product <= len(self.product)
                break
            except AssertionError:
                print(f"Saisissez une chiffre entre 1 et {len(self.product)}.")
            except ValueError:
                print(f"Saisissez un chiffre entre 1 et {len(self.product)} non une lettre.")
        self.dict_product = [x for x in self.product if x["choice"] == self.answer_product][0]
    
    def subsitue(self):
        print("*************************************")
        print(f"Voici un produit de substitution  à : {self.dict_product['product'].name} avec un nutriscore de : {self.dict_product['product'].nutriscore}")
        print("*************************************")
        p=Product()
        for row in p.find_healthy(self.dict_product["product"],self.answer_category):
            stores = ", ".join([store.name.capitalize() for store in row.stores])
            print(f"Nom du produit: {row.name}, Nutriscore : {row.nutriscore}, Magasins où l'acheter {stores}")
        print("Souhaitez vous sauvegarder dans vos favoris le substitut et le produit substitué ? [y] or [n]")

    def main(self):
        self.home()
        self.category_choice()
        self.product_choice()
        self.subsitue()


if __name__ == "__main__":
    
    a = Client()
    a.main()
    