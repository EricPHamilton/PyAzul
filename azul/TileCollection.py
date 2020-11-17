from .TileColor import TileColor
import numpy as np

class TileCollection():
    def __init__(self, numBlue, numYellow, numRed, numBlack, numCyan, numWhite):
        self.tiles = [numBlue, numYellow, numRed, numBlack, numCyan, numWhite]

    def copy(self):
        return TileCollection(self.tiles[0], self.tiles[1], self.tiles[2], self.tiles[3], self.tiles[4], self.tiles[5])
    
    def equals(self, col):
        return self.tiles == col.tiles

    def display(self):
        print("Lid:",self.tiles)
    
    def clear(self):
        self.tiles = [0, 0, 0, 0, 0, 0]
    
    def toString(self):
        return str(self.tiles)
    
    def getOutputString(self):
        return str(self.tiles[0]) + "\t" + str(self.tiles[1]) + "\t" + str(self.tiles[2]) + "\t" + str(self.tiles[3]) + "\t" + str(self.tiles[4]) + "\t" + str(self.tiles[5])
    
    def getCount(self):
        sum = 0
        for numColor in self.tiles:
            sum += numColor
        return sum
    
    def getCountOfColor(self, color: TileColor):
        return self.tiles[color.value]
    
    def setCountOfColor(self, color: TileColor, count: int):
        self.tiles[color.value] = count
    
    def pickRandomTiles(self, count, rand):
        sample = [TileColor.BLUE] * self.tiles[0] + [TileColor.YELLOW] * self.tiles[1] + [TileColor.RED] * self.tiles[2] + [TileColor.BLACK] * self.tiles[3] + [TileColor.CYAN] * self.tiles[4]
        randSample = rand.sample(sample, count)

        retTiles = TileCollection(0, 0, 0, 0, 0, 0)

        for tile in randSample:
            self.removeTiles(tile, 1)
            retTiles.addTiles(tile, 1)
        
        return retTiles

    def addTiles(self, color, count):
        self.tiles[color.value] += count
    
    def addTilesFromCollection(self, collection):
        for i in range(6):
            self.tiles[i] += collection.tiles[i]

    def removeTiles(self, color, count):
        self.tiles[color.value] -= count
        if self.tiles[color.value] < 0:
            print("Removed tiles that didn't exist: ", color, count)
            exit(0)
    
    # Moves all tiles in this collection to a destination
    def moveAllTiles(self, dest):
        for color in TileColor:
            count = self.getCountOfColor(color)
            dest.addTiles(color, count)
            self.removeTiles(color, count)
    
    def getArray(self):
        return np.array(self.tiles)
    
    @staticmethod
    def getFromArray(arr):
        return TileCollection(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])