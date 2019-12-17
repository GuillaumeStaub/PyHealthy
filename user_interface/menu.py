from user_interface.client import Client


class Menu():
    """This class articulates all Client methods between them.
    """
    def __init__(self):
        """Initializes the Client, and stores the client methods
        in a dictionary each method attached to an integer.
        """
        self.client = Client()
        self.actual = 1
        self.next = None
        self.back = None
        self.answer = None
        self.menus = {
            1: self.client.home,
            2: self.client.category_choice,
            3: self.client.product_choice,
            4: self.client.subsitue,
            5: self.client.display_favorites}

    def next_menu(self):
        """Call up the next "menu".
        """
        self.actual += 1

    def back_menu(self):
        """Call up the back "menu".
        """
        self.actual -= 1

    def actual_menu(self):
        """Lets you manage the current menu by setting menus
        around (previous and next).
        """
        self.back = self.actual - 1
        self.next = self.actual + 1
        self.answer = self.menus[self.actual]()

    def tree(self):
        """This tree is the articulation of the whole program.
         Everything is defined and set up so that anywhere in the program
        the user can go back.
        """
        while True:
            self.actual_menu()
            if self.client.answer_home == 1:
                self.actual = 1
            elif self.client.answer_home == 2 and self.actual == 1:
                self.actual = 4
                self.client.answer = 0
            elif self.client.answer_home == "b":
                self.actual = 0
            elif self.actual == 4:
                self.actual = 0
            elif self.actual == 5:
                self.actual = 0
            elif str(self.answer).lower() == "b":
                self.back_menu()
                break
            self.next_menu()


def main():
    """Initialize the menu and launch the tree function
    """
    m = Menu()
    if m.client.verify_db():
        while True:
            m.tree()


if __name__ == "__main__":
    pass
