from .Player import Player
from .TileColor import TileColor

class AzulAction:
    def __init__(self, player: Player, source, color: TileColor, line):
        self.player = player
        self.source = source
        self.color = color
        self.line = line
    
    def toString(self):
        return str(self.player.id) + ", " + str(self.source) + ", " + str(self.color) + ", " + str(self.line)
    
    def getActionInt(self) -> int:
        # location = actionInt // 30
        # color = (actionInt % 30) // 6
        # line = (actionInt % 30) % 6
        sum = 0
        sum += self.source * 30
        sum += self.color.value * 6
        sum += int(self.line)
        return sum
