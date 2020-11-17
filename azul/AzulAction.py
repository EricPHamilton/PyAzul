from .TileColor import TileColor

class AzulAction:
    def __init__(self, playerID: id, source, color: TileColor, line):
        self.playerID = playerID
        self.source = source
        self.color = color
        self.line = line
    
    def toString(self):
        return str(self.playerID) + ", " + str(self.source) + ", " + str(self.color) + ", " + str(self.line)
    
    def getActionInt(self) -> int:
        # location = actionInt // 30
        # color = (actionInt % 30) // 6
        # line = (actionInt % 30) % 6
        sum = 0
        sum += self.source * 30
        sum += self.color.value * 6
        sum += int(self.line)
        return sum
    
    def getTurnExplanationString(self) -> str:
        if self.source <= 4:
            source = "factory #" + str(self.source + 1)
        else:
            source = "the center"
        
        if self.line <= 4:
            line = "line " + str(self.line + 1)
        else:
            line = "the floor line"

        return str(f"Player {self.playerID} took {self.color.name} tiles from {source} and put them on {line}")
