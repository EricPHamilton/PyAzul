from .TileColor import TileColor
from .TileCollection import TileCollection

class PlayerLines():
    def __init__(self):
        self.lines = []
        self.lines.append([1, None, 0])
        self.lines.append([2, None, 0])
        self.lines.append([3, None, 0])
        self.lines.append([4, None, 0])
        self.lines.append([5, None, 0])
    
    def toString(self):
        string = ""
        for i in range(5):
            if (self.lines[i][2] == 0): 
                countColorString = "None"
            else:
                countColorString = str(self.lines[i][2]) + " " + self.lines[i][1].name
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
        
        retCollection = TileCollection(0, 0, 0, 0, 0, 0)
        retCollection.addTiles(color, overflowCount)
        return retCollection
        