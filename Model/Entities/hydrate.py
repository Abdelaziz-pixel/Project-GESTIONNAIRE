from Model.conference import *
from Model.speaker import *

class Hydrate():

    def __init__(self,data):
        self.hydrate(data)

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)


    

    