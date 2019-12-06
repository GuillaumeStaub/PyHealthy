import sys

from pyfiglet import Figlet


from database.category import Category
from database.product import Product
from database.favorites import Favorites

from config.session import Session
from config.constants import prCyan, prPurple, prRed, prYellow


class Client():
    """This class contains all methods for displaying menus,
    and interacting with the user.

    """

    def __init__(self):
        """Initializes all user responses for each menu to None,
        all containers that store products, favorites etc ... are flushed.
        """
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
        """Corresponds to the main menu This method offers two options
        to the user. Depending on his answer he will access the requested
        menu.
        """
        self.answer_home = None
        self.answer_category = None
        self.subsitue_answer = None
        self.answer_product = None
        f = Figlet(font='slant')
        prPurple(f.renderText('Welcome on PyHealthy'))
        print(f"Bienvenue sur PyHealthy, l'application qui a pour but de"
              f"mettre un peu plus de sains dans votre vie.")
        prRed(
            f"À tout moment dans le programme faites [q]"
            f"pour quitter ou [b] pour revenir au menu principal")
        print("Que souhaitez-vous faire ? ")
        prCyan("1. Voulez-vous substituer un produit ? ")
        prCyan("2. Voulez-vous accéder à vos aliments déjà substitués ?")
        self.answer_home = self.input_answer(self.answer_home, 2)

    def category_choice(self):
        """This method corresponds to the choice menu of the category.
        The query in Categories is used to retrieve all categories.
        The categories are stored in a dictionary associating the id
        of the category to the category. Then the dictionary is displayed
        in an orderly way and the user makes his choice.

        Returns:
            int or str: Corresponds to the choice of the user.
        """
        self.answer_home = 0
        self.answer_product = 0
        print(f"Choisissez une catégorie parmi les suivantes"
              f"en tapant le chiffre correspondant:")
        c = Category()
        self.dict_category = {
            row.id: row.name for row in c.select_categories(
                self.session)}
        [prCyan(f"{x}. {y.capitalize()}")
         for x, y in sorted(self.dict_category.items())]
        self.answer_category = self.input_answer(
            self.answer_category, len(self.dict_category))
        self.product = []
        self.gen_product()
        return self.answer_category

    def product_choice(self):
        """This method offers a choice of 10 products to the
        user according to the category chosen previously.
        Products methods are called to retrieve the products.
        They are associated with a number in a dict and stored in a list.
        The user makes his choice and the product chosen
        and stored in a variable.

        Returns:
            int or str: this answer makes it possible
            to decide on the following of the program.
        """
        print("*************************************")
        print(f"Voici la liste des produits non sains."
              f"Tapez le chiffre correspondant au produit de votre choix")
        for dictio in self.product:
            prCyan(
                f"\033[95m{dictio['choice']}"
                f".\033[0m {repr(dictio['product'])}")
        self.answer_product = self.input_answer(
            self.answer_product, len(self.product))
        if self.answer_product not in ["b", "B"]:
            self.fat_product = [
                x["product"] for x in self.product
                if x["choice"] == self.answer_product][0]
        else:
            return self.answer_product

    def subsitue(self):
        """This method allows to generate a substitute for the product
        previously selected thanks to the request contained in Product
        that looks for a product with a better Nutriscore. Then the user
        decides whether to save the result in the Favorites table,
        whether to leave the program or to return to the main menu.

        Returns:
            str: this answer makes it possible to decide
            on the following of the program.
        """
        print("*************************************")
        prYellow(f"Vous avez sélectionné: {self.fat_product}")
        p = Product()
        prPurple("Voici un produit plus sain dans la même catégorie: ")
        self.healthy_product = p.find_healthy(
            self.session, self.fat_product, self.answer_category)
        print(repr(self.healthy_product) +
              f" \033[94m Magasins où acheter:\033[0m"
              f"{self.healthy_product.format_stores}")
        prCyan(
            f"Souhaitez-vous sauvegarder dans vos favoris"
            f"le substitut et le produit substitué ? [y] or [n]")
        while True:
            self.subsitue_answer = input("Votre choix : ")
            if self.subsitue_answer in ["q", "Q"]:
                sys.exit()
            elif self.subsitue_answer in ["b", "B"]:
                return self.subsitue_answer
            elif self.subsitue_answer.lower() == "y":
                self.save_products()
                prYellow(f"Produit sauvegardé dans la"
                         f"base de données avec succès")
                prCyan("Voulez-vous retourner au menu principal [y] ou [n]")
                self.subsitue_answer = input("Vottre choix :")
                if self.subsitue_answer.lower() == "n":
                    sys.exit()
                elif self.subsitue_answer.lower() == "y":
                    break
                else:
                    prRed("[y] pour quitter ou [n] pour aller au menu")
            elif self.subsitue_answer.lower() == "n":
                prCyan(
                    f"Vous ne souhaitez pas enregistrer le substitut."
                    f"Souhaitez-vous quitter le programme ou retourner"
                    f"au menu principal?")
                prCyan("[q] pour quitter ou [m] pour aller au menu")
                self.subsitue_answer = input("Vottre choix :")
                if self.subsitue_answer.lower() == "q":
                    sys.exit()
                elif self.subsitue_answer.lower() == "m":
                    break
                else:
                    print("[q] pour quitter ou [m] pour aller au menu")
            else:
                print("[y] ou [n]")

    def gen_product(self):
        """This method generates the list of 10 products to display.
        """
        p = Product()
        i = 1
        for row in p.select_products(self.session, self.answer_category):
            self.product.append({"choice": i, "product": row})
            i += 1

    def load(self):
        """This method allows you to retrieve all favorites,
        retrieve the product associated with the favorites and
        store in a dictionary the healthy product and the
        fat product itself stored in a list.
        The method works depending on whether
        it detects any favorites in the table.
        """
        p = Product()
        f = Favorites()
        result = [row for row in f.select_favorites(self.session)]
        if result != []:
            for fav in result:
                self.favorites.append(
                    {
                        "fat_product": p.load_product(
                            fav.fat_product,
                            self.session),
                        "healthy_product": p.load_product(
                            fav.healthy_product,
                            self.session)})
        else:
            print("Actuellement aucun favori n'a été sauvegardé")

    def save_products(self):
        """This method saves the substituted product associated
        with the substitute in the database's Favorite Table.
        """
        favorite = Favorites(
            fat_product=self.fat_product.id,
            healthy_product=self.healthy_product.id)
        self.session.add(favorite)
        self.session.commit()

    def display_favorites(self):
        """This method retrieves the favorite dictionary and displays
        all the favorites. The user therefore makes the choice
        to return to the menu or to leave.
        """
        self.answer_home = 0
        self.load()
        for f in self.favorites:
            prYellow("Le produit substitué est :")
            print(f["fat_product"])
            prYellow("Le substitut est :")
            print(f["healthy_product"])
            print(f"*****************************"
                  f"************************************")
            print()
        prCyan(f"Souhaitez-vous quitter le programme"
               f"ou retourner au menu principal?")
        prCyan("[q] pour quitter ou [m] pour aller au menu")
        while True:
            self.answer_favorites = input("Votre choix: ")
            if self.answer_favorites.lower() == "q":
                sys.exit()
            elif self.answer_favorites.lower() == "m":
                break

    def input_answer(self, answer, size):
        """This method is one of the central elements of the class.
        It allows to interact with the user and to act according to his answer.

        Args:
            answer (int or str): this answer makes it possible
            to decide on the following of the program
            size (int): Number of items displayed

        Returns:
            str or int: this answer makes it possible
            to decide on the following of the program
        """
        while True:
            answer = input("Votre choix : ")
            if answer in ["q", "Q"]:
                sys.exit()
            elif answer in ["b", "B"]:
                return answer
            try:
                answer = int(answer)
                assert answer > 0 and answer <= size
                break
            except AssertionError:
                prRed(f"Saisissez un chiffre entre 1 et {size}.")
            except ValueError:
                prRed(
                    f"Saisissez un chiffre entre 1 et"
                    f" {size} et non une lettre.")
        return answer


if __name__ == "__main__":
    pass
