"""import of the connection from the Model folder and module datetime
    importation de la connexion depuis le dossier Model et du module datetime"""

from Model.Entities.hydrate import *
import datetime

class Conference():
    
    """Constructor containing the connection and attributes specific to the conference
            Constructeur contenant la connexion et les attributs propre a la conférence"""
    def __init__(self, data):
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
        return """\nTitre : {}\nResumé: {}\nDate et heure: {}\nSpeaker_id: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.titre, self.resume, self.date_heure, self.speaker_id)
    