from __future__ import unicode_literals,print_function
from pyfiglet import Figlet



from PyInquirer import prompt, Separator, style_from_dict
class Client():

    def __init__(self):
        f = Figlet(font='slant')
        print (f.renderText('Welcome on PyHealthy'))
        


    def home(self):
        questions = [
        {
        'type': 'rawlist',
        'name': 'home_choice',
        'message': 'Que souhaitez-vous faire ? ',
        'choices':["Substituer un aliment", "Accéder à mes aliments déjà substitués.", Separator(), "Quitter le programme?"],
        'default':"1"
        }
        ]
        answers = prompt(questions)
        return answers

if __name__ == "__main__":
    
    a = Client()
    while True:
        a.home()