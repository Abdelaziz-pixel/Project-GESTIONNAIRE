from Model.speaker import *

if __name__ == "__main__":
    

    Choice=""
    while Choice != 'q':
        print("Créer une conférence [C], Créer un conférencier [A]")
        Choice = input("Que souhaitez-vous faire ?").upper()
        if Choice == "C":
            test = Speaker()
            test.create_speaker()
        if Choice == "Q":
            print("À bientôt pour un prochain évènement ;-)")
            exit()
            