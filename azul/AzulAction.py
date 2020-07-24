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
