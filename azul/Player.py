from .Wall import Wall
from .FloorLine import FloorLine
from .PlayerLines import PlayerLines
from .TileCollection import TileCollection
from .TileColor import TileColor
from .AzulAction import AzulAction

class Player:
    def __init__(self, id):
        self.id = id
        self.wall = Wall()
        self.floorLine = FloorLine()
        self.playerLines = PlayerLines()
    
    def toString(self):
        return str(self.id) + "\n" + self.playerLines.toString() + self.wall.toString() + self.floorLine.toString()
    
    def display(self):
        print(self.toString())
    
    def placeTilesFromAction(self, action: AzulAction, tiles: TileCollection) -> TileCollection:
        # If we picked the white tile, place it on the floor line.
        if tiles.getCountOfColor(TileColor.WHITE) > 0:
            self.floorLine.tileCollection.addTiles(TileColor.WHITE, 1)
            tiles.removeTiles(TileColor.WHITE, 1)
        
        # Place the rest of the tiles on the chosen line
        color = TileColor(action.color)
        count = tiles.getCountOfColor(color)
        if action.line < 5:
            overflowForFloorLine = self.playerLines.placeTiles(action.line, color, count)
            
            # TODO: Need to implement playerlines place tiles and add overflow to the floor line.
        else:
            # add to floor line and calc overflow for lid
            overflowNum = max(7 - (self.floorLine.tileCollection.getCount() + count), 0)
            overflowCollection = TileCollection(0, 0, 0, 0, 0, 0)
            overflowCollection.addTiles(color, overflowNum)
            tiles.removeTiles(color, overflowNum)
            tiles.moveAllTiles(self.floorLine.tileCollection)
            return overflowCollection


        