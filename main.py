from Model.speaker import *

if __name__ == "__main__":
    
    Choice=""
    Speak = Speaker()
    while Choice != 'q':
        print("Créer un speaker [C], Créer une conférence [A]")
        print("Supprimer un speaker [D], Supprimer une conférence [S]")
        Choice = input("Que souhaitez-vous faire ?").upper()
        if Choice == "C":
            Speak.create_speaker()
        if Choice == "D":
            Speak.delete_speaker()
        if Choice == "Q":
            print("À bientôt pour un prochain évènement ;-)")
            exit()
            