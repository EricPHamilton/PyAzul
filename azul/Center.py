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
        print(self.toString())

    def toString(self):
        retStr = "Loc\tBlue\tYellow\tRed\tBlack\tCyan\tWhite\n"
        for i in range(5):
            retStr += ("Fac_" + str(i) + ":" + self.factories[i].toString() + "\n")
        
        retStr += ("Cent:" + self.center.toString() + "\n")
        return retStr   
    
    def countTiles(self, location, color):
        if location != 5:
            return self.factories[location].tiles.getCountOfColor(color)
        elif location == 5:
            return self.center.getCountOfColor(color)
        else:
            print("invalid location:", location)
            exit(1)
        