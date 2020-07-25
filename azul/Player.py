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
        self.score = 0
    
    def toString(self):
        return str(self.id) + "\n" + self.playerLines.toString() + self.wall.toString() + self.floorLine.toString()
    
    def display(self):
        print(self.toString())
    
    def finishRound(self) -> TileCollection:
        wallScore = 0
        floorScore = self.floorLine.getScore()
        tilesFromLines = TileCollection(0, 0, 0, 0, 0, 0)

        for line in self.playerLines.lines:
            color = line[1]
            if color != None:
                if line[0] == line[2]:
                    wallScore += self.wall.addTile(line[0] - 1, color)
                    tilesFromLines.addTiles(color, line[0] - 1) # We moved one tile to the wall, so it's num - 1.
                else:
                    tilesFromLines.addTiles(color, line[2])
        
        self.score = max(wallScore - floorScore, 0)
        return tilesFromLines

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
            count = overflowForFloorLine.getCount()
            tiles = overflowForFloorLine

        # add to floor line and calc overflow for lid
        overflowNum = max((self.floorLine.tileCollection.getCount() + count) - 7, 0)
        overflowCollection = TileCollection(0, 0, 0, 0, 0, 0)
        overflowCollection.addTiles(color, overflowNum)
        tiles.removeTiles(color, overflowNum)
        tiles.moveAllTiles(self.floorLine.tileCollection)
        return overflowCollection


        