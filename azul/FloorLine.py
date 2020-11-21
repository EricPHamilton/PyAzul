from .TileCollection import TileCollection

class FloorLine():
    def __init__(self):
        self.tileCollection = TileCollection()

    def display(self):
        print("FLOOR LINE:")
        print(self.toString())

    def toString(self):
        return self.tileCollection.toString()
    
    def getScore(self) -> int:
        scoresArray = [0, -1, -2, -4, -6, -8, -11, -14]
        count = min(self.tileCollection.getCount(), 7)
        return scoresArray[count]


        