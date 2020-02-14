"""import of speaker, conference, display and view classes
    importation des classes speaker, conference, display et view"""
from Model.speaker import *
from Model.conference import *
from Model.display import *
from View.View_conf_speak import *

class Controller():

    def Choice(self):
    """instantiation of the Display and view class
            instantiation de la class Diplay et View"""
        display = Display()
        view = View(display)

        Choice=""
        while Choice != 'q':

            view.lancement()
            Choice = input("Que souhaitez-vous faire ?").upper()

            if Choice == "K":
                view.lancement_speak()
                Choice = input("Que souhaitez-vous faire ?").upper()
                if Choice == "P":
                    display.create_speaker()
                if Choice == "Y":
                    display.delete_speaker()
                if Choice == "T":
                    display.show_speak()
                if Choice == "Q":
                    print("a bientot")

            if Choice == "W":
                view.lancement_conf()
                Choice = input("Que souhaitez-vous faire ?").upper()
                if Choice == "H":
                    display.create_conference()
                if Choice == "O":
                    display.delete_conference()
                if Choice == "N":
                    display.show_conference()
                    view.get_all()

            if Choice == "R":
                print("À bientôt pour une prochaine conférence ;-)")
                exit()
            