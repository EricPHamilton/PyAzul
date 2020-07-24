from .TileCollection import TileCollection

class FloorLine():
    def __init__(self):
        self.tileCollection = TileCollection(0, 0, 0, 0, 0, 0)

    def display(self):
        print("FLOOR LINE:")
        print(self.toString())

    def toString(self):
        return self.tileCollection.toString()