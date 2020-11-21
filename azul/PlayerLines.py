from .TileColor import TileColor
from .TileCollection import TileCollection

class PlayerLines():
    def __init__(self):
        self.lines = [
            [1, None, 0],
            [2, None, 0],
            [3, None, 0],
            [4, None, 0],
            [5, None, 0]
        ]
    
    def toString(self):
        string = ""
        for i in range(5):
            if (self.lines[i][2] == 0): 
                countColorString = "None"
            else:
                countColorString = str(self.lines[i][2]) + " " + self.lines[i][1].name[0:3]
            string += ("Line " + str(i + 1) + ": ") + countColorString + "\n"
        return string[:-1]
    
    def isActionValid(self, color, line):
        if line != 5 and self.lines[line][0] == self.lines[line][2]:
            return False
        
        if line != 5 and self.lines[line][1] != None and color != self.lines[line][1]:
            return False
        
        return True
    
    def placeTiles(self, line, color, count) -> TileCollection:
        lineTuple = self.lines[line]
        lineTuple[1] = color
        overflowCount = max(lineTuple[2] + count - lineTuple[0], 0)
        lineTuple[2] = min(lineTuple[2] + count, lineTuple[0])
        
        retCollection = TileCollection()
        retCollection.addTiles(color, overflowCount)
        return retCollection
    
    def getAllTiles(self) -> TileCollection:
        tiles = TileCollection()
        for line in self.lines:
            if line[1] is not None:
                tiles.addTiles(line[1], line[2])
        return tiles
        