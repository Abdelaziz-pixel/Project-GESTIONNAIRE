"""import of the connection from the Model folder
    importation de la connexion depuis le dossier Model"""
from Model.connection import *

    """class speaker
            class conférencier"""
class Speaker():
    
    """Constructor containing the connection and attributes specific to the speaker
            Constructeur contenant la connexion et les attributs propre au conférencier"""
    def __init__(self):
        self.choice = connection()
        self.prenom = None
        self.nom = None
        self.description = None
        self.prefession = None
        self.statut = True 
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
        print(speaker)