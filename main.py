from Model.speaker import *
from Model.conference import *

if __name__ == "__main__":
    
    print("+--------------------------------------------------+")
    print("|---------- GESTIONNAIRE DES CONFERENCES ----------|")
    print("+--------------------------------------------------+")

    Choice=""
    Speak = Speaker()
    Conf = Conference()
    while Choice != 'q':
        print("+-------- Action ----------|-------- Touche -------+")
        print("|     Créer un speaker     |          [P]          |")
        print("|   Supprimer un speaker   |          [Y]          |")
        print("|      Voir un speaker     |          [T]          |")
        print("|   Créer une conférence   |          [H]          |")
        print("| Supprimer une conférence |          [O]          |")
        print("|   Voir une conférence    |          [N]          |")
        print("+--------------------------------------------------+")

        Choice = input("Que souhaitez-vous faire ?").upper()
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
            print("À bientôt pour une prochaine conérence ;-)")
            exit()
            