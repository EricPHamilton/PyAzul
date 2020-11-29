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
        self.hasWhiteTile = False
    
    def toString(self):
        return str(self.id) + "\n" + self.playerLines.toString() + self.wall.toString() + self.floorLine.toString()
    
    def display(self):
        print("Player:", self.id, "\tScore:", self.score)

        playerLineStrings = self.playerLines.toString().split("\n")
        wallStrings = self.wall.toString().split("\n")
        linesAndWall = ""
        for i in range(5):
            addition = (playerLineStrings[i] + "\t\t\t" + wallStrings[i] + "\n")
            linesAndWall += addition

        print(linesAndWall[:-1])

        print("Floor line:", self.floorLine.tileCollection.getCount())
    
    def finishRound(self) -> tuple:
        wallScore = [0, 0] # First is "standard score", second is "bonus" score.
        floorScore = self.floorLine.getScore()

        tilesToLid = self.floorLine.tileCollection.copy()
        tilesToLid.setCountOfColor(TileColor.WHITE, 0)
        self.floorLine.tileCollection.clear()

        for line in self.playerLines.lines:
            color = line[1]
            if color != None:
                if line[0] == line[2]:
                    scores = self.wall.addTile(line[0] - 1, color)
                    wallScore[0] += scores[0]
                    wallScore[1] += scores[1] 

                    tilesToLid.addTiles(color, line[0] - 1) # We moved one tile to the wall, so it's num - 1.
                    line[1] = None
                    line[2] = 0
        
        self.score += max(wallScore[0] + floorScore, 0) + wallScore[1]
        return tilesToLid

    def placeTilesFromAction(self, action: AzulAction, tiles: TileCollection) -> TileCollection:
        # If we picked the white tile, place it on the floor line.
        if tiles.getCountOfColor(TileColor.WHITE) > 0:
            if self.floorLine.tileCollection.getCount() == 7:
                # Yikes. This is a heck of a situation that isn't covered in the rule book. Where do
                # we put the white tile if the floor line is full already?
                # I'm placing it "on the side of the board". Ie, the player still 'has' it, but it's
                # not in the floor line and it's not in the lid. It's in a weird limbo.
                print("Hit that weird white tile state.")
                tiles.removeTiles(TileColor.WHITE, 1)
                self.hasWhiteTile = True
            else:
                self.floorLine.tileCollection.addTiles(TileColor.WHITE, 1)
                tiles.removeTiles(TileColor.WHITE, 1)
                self.hasWhiteTile = True
        
        # Place the rest of the tiles on the chosen line
        if action.dest < 5:
            tilesForFloorLine = self.playerLines.placeTiles(action.dest, action.color, tiles.getCount())
        else:
            tilesForFloorLine = tiles

        # add to floor line and calc overflow for lid
        overflowCollection = TileCollection()
        if tilesForFloorLine.getCount() > 0:
            tilesForFloorLine.moveAllTiles(self.floorLine.tileCollection)
            floorCount = self.floorLine.tileCollection.getCount()
            if floorCount > 7:
                overflowNum = floorCount - 7
                overflowCollection.addTiles(action.color, overflowNum)
                self.floorLine.tileCollection.removeTiles(action.color, overflowNum)
        
        return overflowCollection
        
    def getAllTiles(self):
        tiles = TileCollection()
        tiles.addTilesFromCollection(self.floorLine.tileCollection)
        tiles.addTilesFromCollection(self.playerLines.getAllTiles())
        tiles.addTilesFromCollection(self.wall.getAllTiles())
        return tiles

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
        
        arr[7][5] = int(self.hasWhiteTile)
        
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
        
        retPlayer.hasWhiteTile = bool(arr[7][5])
        
        return retPlayer
        