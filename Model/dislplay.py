from Model.connection import *
from Model.speaker import *
from Model.conference import *

class Display():

    def __init__(self):
        self.choice = connection()

    """Method for creating the speaker containing the necessary query
             Méthode pour la création du conférencier contenant la requête necessaire"""
    def create_speaker(self):
        self.choice.initialize_connection()
        self.prenom = input("Quel est votre prénom ? ")
        self.nom = input("Quel est votre nom ? ")
        self.description = input("Ajoutez une description : ")
        self.profession = input("Quel est votre prefession ? ")
        self.choice.cursor.execute("INSERT INTO Speaker(prenom, nom, description, profession) VALUES (%s, %s, %s, %s)",(self.prenom,self.nom,self.description,self.profession))
        self.choice.connection.commit()
        self.choice.close_connection()

    """Method for deleting the speaker containing the necessary request
            Méthode pour la suppression du conférencier contenant la requête necessaire"""
    def delete_speaker(self):
        self.choice.initialize_connection()
        self.prenom = input("Quel est votre prénom ? ")
        self.nom = input("Quel est votre nom ? ")
        self.choice.cursor.execute("DELETE FROM Speaker WHERE prenom=%s AND nom=%s;",(self.prenom,self.nom))
        self.choice.connection.commit()
        self.choice.close_connection()

    """Method for reading the speaker containing the necessary request
             Méthode pour la lecture du conférencier contenant la requête necessaire"""
    def read_speaker(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM Speaker;")
        speaker = self.choice.cursor.fetchall()
        self.choice.close_connection
        for key, value in enumerate(speaker):
            speaker[key] = Speaker(value)
        return speaker

    def show_speak(self):
        speakers = self.read_speaker()
        if speakers:
            for i in speakers:
                print(i)

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
        for key, value in enumerate(conference):
            conference[key] = Conference(value)
        return conference

    def show_conference(self):
        conferences = self.read_conference()
        if conferences:
            for i in conferences:
                print(i)

