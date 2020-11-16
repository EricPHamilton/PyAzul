from .TileCollection import TileCollection
from .Factory import Factory
from .AzulAction import AzulAction
from .TileColor import TileColor

class Center():
    def __init__(self, bag):
        self.factories = []
        for _ in range(5):
            self.factories.append(Factory(bag))

        # Start with a white tile in the center
        self.center = TileCollection(0, 0, 0, 0, 0, 1) 
    
    def display(self):
        print("\tBlu(1)\tYel(2)\tRed(3)\tBla(4)\tCya(5)\tWhi(6)")
        for i in range(5):
            string = "Fac #" + str(i + 1) + ":\t"
            string += (self.factories[i].tiles.getOutputString() + "\t")
            print(string)
        string = "Center:\t" + self.center.getOutputString()
        print(string)
        
        

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
    
    def takeTiles(self, action: AzulAction) -> TileCollection:
        if action.source < 5:
            isCenter = False
            sourceCollection = self.factories[action.source].tiles
        else:
            isCenter = True
            sourceCollection = self.center
        
        count = sourceCollection.getCountOfColor(action.color)
        retCollection = TileCollection(0, 0, 0, 0, 0, 0)
        retCollection.addTiles(action.color, count)
        sourceCollection.removeTiles(action.color, count)

        if isCenter:
            # check for white tile
            if sourceCollection.getCountOfColor(TileColor.WHITE) > 0:
                retCollection.addTiles(TileColor.WHITE, 1)
                sourceCollection.removeTiles(TileColor.WHITE, 1)
        else:
            # Place other tiles in the center
            sourceCollection.moveAllTiles(self.center)

        return retCollection


        