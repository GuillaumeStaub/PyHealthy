from user_interface.client import Client

class Menu():
    def __init__(self):
        self.client = Client()
        self.actual = 1
        self.next = None
        self.back = None
        self.answer = None
        self.menus = {1:self.client.home, 2:self.client.category_choice, 3:self.client.product_choice, 4:self.client.subsitue, 5:self.client.display_favorites}


    def next_menu(self):
        self.actual += 1
    

    def back_menu(self):
        self.actual -= 1
        


    def actual_menu(self):
        self.back = self.actual - 1
        self.next = self.actual + 1
        self.answer = self.menus[self.actual]()


    def arborescence(self):
        while True : 
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
    m = Menu()
    while True : 
        m.arborescence()

if __name__ == "__main__":
    pass