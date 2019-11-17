from product_downloader import ProductDownloader
from config.constants import search_terms


class ProductCleaner:
    """This class instantiates the ProductDownloader class.
    It recovers the raw data list and cleans them of useless or
    unusable items.

    Returns:
        list: clean products
    """

    def __init__(self):
        """Method that initializes a list with the ProductDownloader class.
        The search terms are in the constants in the datas folder.
        Gross_productscontains a list of x products.

        """
        self.gross_products = [ProductDownloader(term, 100).recover_product
                               for term in search_terms]

    @property
    def clean_products(self):
        """Method transformed into property takes
        as input the openfoodfacts raw data and retrieves only
        the data that we need for our project.
        Incomplete products are discontinued

        Returns:
            list: A dictionary list, each dictionary contains
            useful informations about a product.
        """
        clean_products = []
        for liste_product in self.gross_products:
            for product in liste_product:
                try:
                    clean_products.append(
                        {"name": product["product_name_fr"],
                         "categories": product["categories_tags"],
                         "nutriscore": product["nutrition_grades"],
                         "url": product["url"],
                         "sotres": product["stores_tags"]})
                except KeyError:
                    pass
        return clean_products


if __name__ == "__main__":
    a = ProductCleaner()
    print(a.clean_products[0])
