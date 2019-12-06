import sys

from pyfiglet import Figlet


from database.category import Category
from database.product import Product
from database.store import Store
from database.favorites import Favorites

from config.session import Session
from config.constants import Base, store_product, prCyan, prPurple, prRed, prLightGray, prYellow



class Client():

    def __init__(self):
        self.answer_home = None
        self.answer_category = None
        self.answer_product = None
        self.subsitue_answer = None
        self.healthy_product = None
        self.answer_favorites = None
        self.fat_product = None
        self.dict_category = {}
        self.product = []
        self.favorites = []
        self.session = Session().session
        
    


    def home(self):
        self.answer_home = None
        self.answer_category = None
        self.subsitue_answer = None
        self.answer_product = None
        f = Figlet(font='slant')
        prPurple(f.renderText('Welcome on PyHealthy'))
        print("Bienvenue sur PyHealthy, l'application qui a pour but de mettre un peu plus de sains dans votre vie.")
        prRed("A tout moment dans le programme faites [q] pour quitter ou [b] pour revenir au menu principal")
        print("Que souhaitez vous faire ? ")
        prCyan("1. Voulez vous substitué un produit ? ")
        prCyan("2. Voulez-vous accéder à vos aliments déjà substitués ?")
        self.answer_home = self.input_answer(self.answer_home, 2)

    def category_choice(self):
        self.answer_home = 0
        self.answer_product = 0
        print("Choisissez une catégories parmi les suivantes en tapant le chiffre correspondant:")
        c = Category()
        self.dict_category = {row.id : row.name for row in c.select_categories(self.session)}
        [prCyan(f"{x}. {y.capitalize()}") for x, y in sorted(self.dict_category.items())]
        self.answer_category = self.input_answer(self.answer_category,len(self.dict_category))
        self.product = []
        self.gen_product()
        return self.answer_category

    def product_choice(self):
        print("*************************************")
        print("Voici la liste des produits non sains. Tapez le chiffre correspondant au produit de votre choix")
        for dictio in self.product:
            prCyan(f"\033[95m{dictio['choice']}.\033[0m {repr(dictio['product'])}")
        self.answer_product = self.input_answer(self.answer_product, len(self.product))
        if self.answer_product not in ["b", "B"]:
            self.fat_product = [x["product"] for x in self.product if x["choice"] == self.answer_product][0]
        else:
            return self.answer_product


    def subsitue(self):
        print("*************************************")
        prYellow(f"Vous avez sélectionné: {self.fat_product}")
        p=Product()
        prPurple("Voici un produit plus sain dans la même catégorie: ")
        self.healthy_product = p.find_healthy(self.session,self.fat_product, self.answer_category)
        print(self.healthy_product)
        prCyan("Souhaitez vous sauvegarder dans vos favoris le substitut et le produit substitué ? [y] or [n]")
        while True : 
            self.subsitue_answer = input("Votre choix : ")
            if self.subsitue_answer in ["q", "Q"]:
                sys.exit()
            elif self.subsitue_answer in ["b", "B"]:
                return self.subsitue_answer
            elif self.subsitue_answer.lower() == "y":
                self.save_products()
                prYellow("Produit sauvegardé dans la base de données avec succès")
                prCyan("Voulez vous retourner au menu principal [y] ou [n]")
                self.subsitue_answer = input("Vottre choix :")
                if self.subsitue_answer.lower() == "n":
                    sys.exit()
                elif self.subsitue_answer.lower() == "y": 
                    break
                else : 
                    prRed("[y] pour quitter ou [n] pour aller au menu")
            elif self.subsitue_answer.lower() == "n":
                prCyan("Vous ne souhaitez pas enregistrer le substitue. Souhaitez vous quitter le programme ou retourner au menu principal?")
                prCyan ("[q] pour quitter ou [m] pour aller au menu")
                self.subsitue_answer = input("Vottre choix :")
                if self.subsitue_answer.lower() == "q":
                    sys.exit()
                elif self.subsitue_answer.lower() == "m": 
                    break
                else : 
                    print("[q] pour quitter ou [m] pour aller au menu")
            else : 
                print("[y] or [n]")

    def load(self):
        p = Product()
        f = Favorites()
        result = [row for row in f.select_favorites(self.session)]
        if result != []:
            for fav in result:
                self.favorites.append({"fat_product":p.load_product(fav.fat_product, self.session), "healthy_product":p.load_product(fav.healthy_product, self.session)} )
        else :
            print("Actuellement aucun favoris n'ont été sauvegardés")

    def save_products(self):
        favorite = Favorites(fat_product=self.fat_product.id, healthy_product=self.healthy_product.id )
        self.session.add(favorite)
        self.session.commit()

    
    def display_favorites(self):
        self.answer_home = 0
        self.load()
        for f in self.favorites:
            prYellow("Le produit substitué est :")
            print(f["fat_product"])
            prYellow("Le substitu est :")
            print(f["healthy_product"])
            print("*****************************************************************")
            print()
        prCyan("Souhaitez vous quitter le programme ou retourner au menu principal?")
        prCyan ("[q] pour quitter ou [m] pour aller au menu")
        while True:
            self.answer_favorites = input("Votre choix: ")
            if self.answer_favorites.lower() == "q":
                sys.exit()
            elif self.answer_favorites.lower() == "m":
                break


    def input_answer(self,answer,size):
        while True : 
            answer = input("Votre choix : ")
            if answer in ["q", "Q"]:
                sys.exit()
            elif answer in ["b", "B"]:
                return answer
            try : 
                answer = int(answer)
                assert answer > 0 and answer <= size
                break
            except AssertionError:
                prRed(f"Saisissez une chiffre entre 1 et {size}.")
            except ValueError:
                prRed(f"Saisissez une chiffre entre 1 et {size} et non une lettre.")
        return answer

    def gen_product(self):
        p=Product()
        i =1
        for row in p.select_products(self.session,self.answer_category):
            self.product.append({"choice":i,"product":row})
            i+=1


    


    
  
        
    
        
        
    
    


if __name__ == "__main__":
    pass