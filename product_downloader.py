import requests


class ProductDownloader:
    """This class takes care of getting the raw data from OpenFoodFacts

    Returns:
        list : List containing raw data from OpenFoodFacts
    """

    def __init__(self, category, page_size):
        """Method that initializes the parameters of the GET request
            to the OpenFoodFacts site.

        Args:
            category (str): A str that serves as a search
            criterion on the OpenFoodFacts API
            page_size (int): Number of products requested
        """
        self.category = category
        self.params = {"json": 1, "tagtype_0": "categories",
                       "tag_contains_0": "contains", "tag_0": self.category,
                       "page_size": page_size, "action": "process"}

    def add_category(self, products):
        """Allows to add in each product recovered via
        the API a key specifying its main category contained in the constants

        Args:
            products (list): A list of products in the form of a dictionary
        """
        for product in products:
            product["main_category"] = self.category

    @property
    def recover_product(self):
        """Method transformed into a property that
        via the requests module processes the GET request
        to the OpenFoodFacts API.

        Returns:
            list : list containing all requested products
        """
        r = requests.get("https://world.openfoodfacts.org/cgi/search.pl",
                         params=self.params)
        products = r.json()["products"]
        self.add_category(products)
        return products


if __name__ == "__main__":
    pass
