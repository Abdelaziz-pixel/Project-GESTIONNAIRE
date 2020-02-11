from Model.speaker import *
from Model.conference import *

if __name__ == "__main__":
    
    Choice=""
    Speak = Speaker()
    Conf = Conference()
    while Choice != 'q':
        print("Créer un speaker [C], Créer une conférence [A]")
        print("Supprimer un speaker [D], Supprimer une conférence [S]")
        print("Voir un speaker [V], Voir une conférence [B]")
        Choice = input("Que souhaitez-vous faire ?").upper()
        if Choice == "C":
            Speak.create_speaker()
        if Choice == "D":
            Speak.delete_speaker()
        if Choice == "V":
            Speak.read_speaker()
        if Choice == "A":
            Conf.create_conference()
        if Choice == "S":
            Conf.delete_conference()


        if Choice == "Q":
            print("À bientôt pour un prochain évènement ;-)")
            exit()
            