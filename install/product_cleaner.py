
class ProductCleaner:
    """This class instantiates the ProductDownloader class.
    It recovers the raw data list and cleans them of useless or
    unusable items.

    Returns:
        list: clean products
    """

    def __init__(self, gross_products):
        """Method that initializes a list with the ProductDownloader class.
        The search terms are in the constants in the datas folder.
        Gross_productscontains a list of x products.

        """
        self.gross_products = gross_products

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
                    if self.is_valid(product["product_name_fr"]) and \
                       self.is_valid(product["stores_tags"]):
                        clean_products.append(
                            {"name": product["product_name_fr"],
                             "categories": product["main_category"],
                             "nutriscore": product["nutrition_grades"],
                             "url": product["url"],
                             "stores": product["stores_tags"]})
                except KeyError:
                    continue
        return clean_products

    def is_valid(self, product):
        """Check if some of the data needed to run the program is present

        Args:
            product (str): contains information that must be NO NULL

        Returns:
            bool: returns true if the information is present if not false
        """
        if product != "" and product != []:
            return True
        else:
            return False


if __name__ == "__main__":
    pass
