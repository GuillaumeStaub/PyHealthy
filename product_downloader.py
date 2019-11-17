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
        self.json = 1
        self.tagtype_0 = "categories"
        self.tag_contains_0 = "contains"
        self.tag_0 = category
        self.page_size = page_size
        self.action = "process"

    @property
    def recover_product(self):
        """Method transformed into a property that
        via the requests module processes the GET request
        to the OpenFoodFacts API.

        Returns:
            list : list containing all requested products
        """
        r = requests.get("https://world.openfoodfacts.org/cgi/search.pl",
                         params=self.__dict__)
        return r.json()["products"]


if __name__ == "__main__":
    pass
