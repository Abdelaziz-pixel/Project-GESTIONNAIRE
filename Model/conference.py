"""import of the connection from the Model folder and module datetime
    importation de la connexion depuis le dossier Model et du module datetime"""
from Model.Entities.entitie import *
# import datetime

class Conference(Hydrate):

    """Constructor containing the connection and attributes specific to the conference
            Constructeur contenant la connexion et les attributs propre a la conférence"""
    def __init__(self, data):
        Hydrate.__init__(self,data)


    def __str__(self):
        return """Titre : {}\n Resumé: {}\n Date et heure: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.titre, self.resume, self.date_heure)
    