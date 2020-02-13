"""import of speaker and conference classes from the Model folder
    importation des classes speaker, conference et entities depuis le dossier Model"""
from Model.speaker import *
from Model.conference import *
from Model.Entities.hydrate import *
from Model.display import *
from View.View_conf import *

"""script launch
    lancement du script"""
if __name__ == "__main__":
    
    """instantiation of the Display and view class
            instantiation de la class Diplay et View"""
    display = Display()
    view = View(display)

    Choice=""
    while Choice != 'q':
        view.lancement()
        Choice = input("Que souhaitez-vous faire ?").upper()
        """All possible actions by the user referring to a specific method
                Toutes les actions possible par l'utilisateur renvoyant à une méthode précise"""
        if Choice == "P":
            display.create_speakern()
        if Choice == "Y":
            display.delete_speaker()
        if Choice == "T":
            display.show_speak()
        if Choice == "H":
            display.create_conference()
        if Choice == "O":
            display.delete_conference()
        if Choice == "N":
            view.get_all()
        if Choice == "Q":
            print("À bientôt pour une prochaine conférence ;-)")
            exit()
        