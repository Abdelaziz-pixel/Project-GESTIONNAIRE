"""import of Conference and Speaker class
    importation de la class Conference et Speaker"""
from Model.conference import *
from Model.speaker import *

class Hydrate():
    """constructor containing the hydrate method
        constructeur contenant la méthode hydrate"""
    def __init__(self,data):
        self.hydrate(data)
    """hydrate method allowing to recover the value corresponding to the value
        méthode hydrate permettant de recupérer la valeur correspondant a la valeur"""
    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)


    

    