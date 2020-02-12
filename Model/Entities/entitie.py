from Model.conference import *
from Model.speaker import *

class Hydrate():

    def __init__(self,data):
        self.id = None
        self.prenom = None
        self.nom = None
        self.profession = None
        self.statut = None
        self.speaker_id = None
        self.description = None
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.hydrate(data)

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

    

    