"""import of the connection from the Model folder and module datetime
    importation de la connexion depuis le dossier Model et du module datetime"""

from Model.Entities.hydrate import *
import datetime

class Conference():
    
    """Constructor containing the connection and attributes specific to the conference
            Constructeur contenant la connexion et les attributs propre a la conférence"""
    def __init__(self, data):
        self.speak_id = None
        self.prenom = None
        self.nom = None
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.speaker_id = None
        self.hydrate(data)

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return """\nTitre : {}\nResumé: {}\nDate et heure: {}\nspeak_id: {}\n Nom du speaker: {}\n Prénom du speaker: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.titre, self.resume, self.date_heure, self.speak_id, self.nom, self.prenom)
    