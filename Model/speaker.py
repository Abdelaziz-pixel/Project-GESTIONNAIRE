"""import of the connection from the Model folder
    importation de la connexion depuis le dossier Model"""

from Model.Entities.hydrate import *
    
class Speaker(Hydrate):
    
    """Constructor containing the connection and attributes specific to the speaker
            Constructeur contenant la connexion et les attributs propre au conférencier"""
    def __init__(self, data):
        self.id_c = None
        self.prenom = None
        self.nom = None
        self.profession = None
        self.statut = None
        self.description = None
        Hydrate.__init__(self,data)
    
    def __str__(self):
        return """ Id: {}\n Prénom: {}\n Nom: {}\n Profession: {}\n Description: {}\n Statut: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.id_c, self.prenom, self.nom, self.profession,self.description, self.statut)
    
    
    
