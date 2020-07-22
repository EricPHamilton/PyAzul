from .TileCollection import TileCollection

class FloorLine():
    def __init__(self):
        self.numTiles = 0
        self.tileCollection = TileCollection(0, 0, 0, 0, 0, 0)
    
    def getCount(self):
        return self.numTiles

    def display(self):
        print("FLOOR LINE:")
        print(self.toString())

    def toString(self):
        return self.tileCollection.toString()