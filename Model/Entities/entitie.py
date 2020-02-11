class Hydrate():

    def __init__(self):
        pass

    def hydrate(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
