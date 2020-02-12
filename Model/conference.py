"""import of the connection from the Model folder and module datetime
    importation de la connexion depuis le dossier Model et du module datetime"""
from Model.connection import *
import datetime

    """class conférence
            class conference"""
class Conference():

    """Constructor containing the connection and attributes specific to the conference
            Constructeur contenant la connexion et les attributs propre a la conférence"""
    def __init__(self):
        self.choice = connection()
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.speaker_id = None

    """Method for creating the conference containing the necessary query
             Méthode pour la création de la conférence contenant la requête necessaire"""
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

    """Method for deleting the conference containing the necessary request
            Méthode pour la suppression de la conférence contenant la requête necessaire"""
    def delete_conference(self):
        self.choice.initialize_connection()
        self.titre = input("Quel est le titre de la conférence ? ")
        self.choice.cursor.execute("DELETE FROM Conference WHERE titre=%s;",(self.titre,))
        self.choice.connection.commit()
        self.choice.close_connection()

    """Method for reading the conference containing the necessary request
             Méthode pour la lecture de la conférence contenant la requête necessaire"""
    def read_conference(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM Conference;")
        conference = self.choice.cursor.fetchall()
        self.choice.close_connection
        print(conference)