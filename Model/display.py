from Model.connection import *
from Model.speaker import *
from Model.conference import *

class Display():

    def __init__(self):
        self.choice = connection()

    def jointure(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT c.titre,c.resume,c.date_heure,c.speaker_id,s.speak_id,s.prenom,s.nom,s.description,s.profession,s.statut FROM Conference AS c LEFT JOIN Speaker AS s ON c.speaker_id = s.speak_id;")
        self.choice.connection.commit()
        rows = self.choice.cursor.fetchall()
        self.choice.close_connection
        liste = list()
        for row in rows:
            liste.append({'titre':row[0],'resume': row[1], 'date_heure':row[2],
            'speaker_id':row[3],'speak_id':row[4], 'prenom': row[5], 'nom':row[6], 'description':row[7], 'profession':row[8], 'statut':row[9] })
        return liste


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
        self.speak_id = input("Quel est votre speak_id ? ")
        self.choice.cursor.execute("DELETE FROM Speaker WHERE speak_id = %s;",(self.speak_id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("Le conférencier a été supprimer !")

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
        self.speaker_id = int(input("Quel est votre id ? "))
        self.date_heure = datetime.datetime(datetime.date.today().year, self.mois,self.jour,self.heure,self.minute,0)
        self.choice.cursor.execute("INSERT INTO Conference(titre, resume, date_heure, speaker_id) VALUES (%s, %s, %s, %s)",(self.titre,self.resume,self.date_heure,self.speaker_id))
        self.choice.connection.commit()
        self.choice.close_connection()

    """Method for deleting the conference containing the necessary request
            Méthode pour la suppression de la conférence contenant la requête necessaire"""
    def delete_conference(self):
        self.choice.initialize_connection()
        self.id = input("Quel est l'id de la conférence ? ")
        self.choice.cursor.execute("DELETE FROM Conference WHERE id=%s;",(self.id,))
        self.choice.connection.commit()
        self.choice.close_connection()

    """Method for reading the conference containing the necessary request
             Méthode pour la lecture de la conférence contenant la requête necessaire"""
    def read_conference(self):
        self.choice.initialize_connection()
        self.choice.cursor.execute("SELECT * FROM Conference ORDER BY date_heure ;")
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

