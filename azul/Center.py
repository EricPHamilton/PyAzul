from .TileCollection import TileCollection
from .Factory import Factory

class Center():
    def __init__(self, bag):
        self.factories = []
        for _ in range(5):
            self.factories.append(Factory(bag))

        # Start with a white tile in the center
        self.center = TileCollection(0, 0, 0, 0, 0, 1) 
    
    def display(self):
        print("Loc\tBlue\tYellow\tRed\tBlack\tCyan\tWhite")
        for i in range(5):
            print("Fac_", i, ":", self.factories[i].toString())
        
        print("Cent:", self.center.toString())