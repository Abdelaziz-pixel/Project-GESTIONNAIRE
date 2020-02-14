"""import of the Hydrate class 
    importation de la class Hydrate"""
from Model.Entities.hydrate import *
    
class Speaker(Hydrate):
    
    """Constructor containing the attributes specific to the Speaker as well as the hydrate method
        Constructeur contenant les attributs propre au Speaker ainsi que la méthode hydrate"""
    def __init__(self, data):
        self.speak_id = None
        self.prenom = None
        self.nom = None
        self.profession = None
        self.statut = None
        self.description = None
        Hydrate.__init__(self,data)
    """method to return the values in the form of a character string
        méthode permettant de retourner les valeurs sous forme de chaine de caractére"""
    def __str__(self):
        return """ Id: {}\n Prénom: {}\n Nom: {}\n Profession: {}\n Description: {}\n Statut: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.speak_id, self.prenom, self.nom, self.profession,self.description, self.statut)
    
    
    
