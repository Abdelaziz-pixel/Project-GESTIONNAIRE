"""import of speaker and conference classes from the Model folder
    importation des classes speaker et conference depuis le dossier Model"""
from Model.speaker import *
from Model.conference import *

"""script launch
    lancement du script"""
if __name__ == "__main__":
    
    """title of programme
            titre du programme"""
    print("+--------------------------------------------------+")
    print("|---------- GESTIONNAIRE DES CONFERENCES ----------|")
    print("+--------------------------------------------------+")

    """instantiation of the Speaker and Conference class
            instantiation de la class Speaker et Conference"""
    Choice=""
    Speak = Speaker()
    Conf = Conference()
    while Choice != 'q':

    """presentation of the possible choices for the user
            présentation des choix possible pour l'utilisateur"""
        print("+-------- Action ----------|-------- Touche -------+")
        print("|     Créer un speaker     |          [P]          |")
        print("|   Supprimer un speaker   |          [Y]          |")
        print("|      Voir un speaker     |          [T]          |")
        print("|   Créer une conférence   |          [H]          |")
        print("| Supprimer une conférence |          [O]          |")
        print("|   Voir une conférence    |          [N]          |")
        print("+--------------------------------------------------+")
        print("|  Quitter le proggramme   |          [Q]          |")
        print("+--------------------------------------------------+")

        Choice = input("Que souhaitez-vous faire ?").upper()
        
        """All possible actions by the user referring to a specific method
                Toutes les actions possible par l'utilisateur renvoyant à une méthode précise"""
        if Choice == "P":
            Speak.create_speaker()
        if Choice == "Y":
            Speak.delete_speaker()
        if Choice == "T":
            Speak.read_speaker()
        if Choice == "H":
            Conf.create_conference()
        if Choice == "O":
            Conf.delete_conference()
        if Choice == "N":
            Conf.read_conference()
        if Choice == "Q":
            print("À bientôt pour une prochaine conférence ;-)")
            exit()
            