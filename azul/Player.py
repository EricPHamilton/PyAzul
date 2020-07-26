from .Wall import Wall
from .FloorLine import FloorLine
from .PlayerLines import PlayerLines
from .TileCollection import TileCollection
from .TileColor import TileColor
from .AzulAction import AzulAction
import numpy as np

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
        print("Player", self.id)
        print(self.playerLines.toString())
        print("Floor line:", self.floorLine.tileCollection.getCount())
    
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
        
        self.score = max(wallScore + floorScore, 0)
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
    
    def getArray(self):
        arr = np.zeros((8, 6))
        arr[0][0] = self.id
        for i in range(5):
            color = self.playerLines.lines[i][1]
            if color is None:
                color = -1
            else:
                color = color.value
            arr[0][i + 1] = color
        arr[1][0] = self.score
        for i in range(5):
            arr[1][i + 1] = self.playerLines.lines[i][2]
        arr[2] = self.floorLine.tileCollection.getArray()
        for i in range(5):
            for j in range(6):
                if j == 5: #This col will never be full. "-2" it so 0s dont get confusing.
                    arr[3 + i][j] = -2
                else:
                    arr[3 + i][j] = int(self.wall.cells[i][j])
        
        return arr

    @staticmethod
    def getFromArray(arr):
        retPlayer = Player(-2)
        retPlayer.id = arr[0][0]
        retPlayer.score = arr[1][0]
        for i in range(5):
            color = arr[0][i + 1]
            if color == -1:
                color = None
            else:
                color = TileColor(color)
            retPlayer.playerLines.lines[i][1] = color
            retPlayer.playerLines.lines[i][2] = arr[1][i + 1]
        retPlayer.floorLine.tileCollection = TileCollection.getFromArray(arr[2])
        for i in range(5):
            for j in range(5):
                retPlayer.wall.cells[i][j] = arr[3 + i][j]
        
        return retPlayer
        