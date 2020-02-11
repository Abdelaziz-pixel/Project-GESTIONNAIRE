from Model.connection import *
import datetime

class Conference():

    def __init__(self):
        self.choice = connection()
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.speaker_id = None

    def create_conference(self):
        self.choice.initialize_connection()
        self.titre = input("Quel est le titre de la conférence ? ")
        self.resume = input("Quel est votre résumé ? ")
        self.mois = int(input(" Quel mois: "))
        self.jour = int(input("Quel jour: "))
        self.heure = int(input("À quel heure: "))
        self.minute = int(input("minutes: ")) 
        self.date_heure = datetime.datetime(datetime.date.today().year, self.mois,self.jour,self.heure,self.minute,0)
        self.choice.cursor.execute("INSERT INTO Conference(titre, resume, date_heure) VALUES (%s, %s, %s)",(self.titre,self.resume,self.date_heure))
        self.choice.connection.commit()
        self.choice.close_connection()

    def delete_conference(self):
        pass

    def read_conference(self):
        pass