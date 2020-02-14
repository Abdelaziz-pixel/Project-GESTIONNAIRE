"""import of the Hydrate class and module datetime
    importation de la class Hydrate et du module datetime"""
from Model.Entities.hydrate import *
import datetime

class Conference():
    
    """Constructor containing the attributes specific to the Conference as well as the hydrate method
            Constructeur contenant les attributs propre a la conference ainsi que la méthode hydrate"""
    def __init__(self, data):
        self.speak_id = None
        self.prenom = None
        self.nom = None
        self.titre = None
        self.resume = None
        self.date_heure = None
        self.speaker_id = None
        self.hydrate(data)
    """hydrate method allowing to recover the value corresponding to the value
        méthode hydrate permettant de recupérer la valeur correspondant a la valeur"""
    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    """method to return the values in the form of a character string
        méthode permettant de retourner les valeurs sous forme de chaine de caractére"""
    def __str__(self):
        return """\nTitre : {}\nResumé: {}\nDate et heure: {}\nspeak_id: {}\n Nom du speaker: {}\n Prénom du speaker: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.titre, self.resume, self.date_heure, self.speak_id, self.nom, self.prenom)
    