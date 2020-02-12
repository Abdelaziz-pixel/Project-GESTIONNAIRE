"""import of the connection from the Model folder
    importation de la connexion depuis le dossier Model"""
from Model.connection import *
from Model.Entities.entitie import *
    #class speaker
            #class conférencier
class Speaker(Hydrate):
    
    """Constructor containing the connection and attributes specific to the speaker
            Constructeur contenant la connexion et les attributs propre au conférencier"""
    def __init__(self, data):
        Hydrate.__init__(self,data)
    
    def __str__(self):
        return """ Id: {}\n Prénom: {}\n Nom: {}\n Profession: {}\n Description: {}\n Speaker_id: {}\n~~~~~~~~~~~~~~~~~~~~~~~~~""".format(self.id, self.prenom, self.nom, self.profession,self.description, self.speaker_id)
    
    
    
