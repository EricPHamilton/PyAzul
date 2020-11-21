from .TileColor import TileColor

class AzulAction:
    # playerID: ID of the player taking the action
    # source: Source of the tiles chosen. 0-4 = factories, 5 = center.
    # color: Color of the tiles chosen.
    # dest: Destination of the tiles. 0-4 = player lines. 5 = floor line.
    def __init__(self, playerID: id, source, color: TileColor, dest):
        self.playerID = playerID
        self.source = source
        self.color = color
        self.dest = dest
    
    @staticmethod
    # Return an AzulAction object given the int of the action and the player ID
    def getActionFromInt(actionInt: int, playerID: int):
        location = actionInt // 30
        color = (actionInt % 30) // 6
        line = (actionInt % 30) % 6

        return AzulAction(player, location, TileColor(color), line)
    
    def toString(self):
        return str(self.playerID) + ", " + str(self.source) + ", " + str(self.color) + ", " + str(self.dest)
    
    def getActionInt(self) -> int:
        # location = actionInt // 30
        # color = (actionInt % 30) // 6
        # dest = (actionInt % 30) % 6
        sum = 0
        sum += self.source * 30
        sum += self.color.value * 6
        sum += int(self.dest)
        return sum
    
    # Returns a verbal string explaining what took place on this turn.
    def getTurnExplanationString(self) -> str:
        if self.source <= 4:
            source = "factory #" + str(self.source + 1)
        else:
            source = "the center"
        
        if self.dest <= 4:
            dest = "line " + str(self.dest + 1)
        else:
            dest = "the floor line"

        return str(f"Player {self.playerID} took {self.color.name} tiles from {source} and put them on {dest}")
