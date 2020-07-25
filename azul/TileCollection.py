from .TileColor import TileColor
import numpy as np

class TileCollection():
    def __init__(self, numBlue, numYellow, numRed, numBlack, numCyan, numWhite):
        self.tiles = [numBlue, numYellow, numRed, numBlack, numCyan, numWhite]

    @staticmethod
    def getColorIndex(color):
        if color == TileColor.BLUE:
            return 0
        elif color == TileColor.YELLOW:
            return 1
        elif color == TileColor.RED:
            return 2
        elif color == TileColor.BLACK:
            return 3
        elif color == TileColor.CYAN:
            return 4
        elif color == TileColor.WHITE:
            return 5

    def display(self):
        print(self.tiles)
    
    def toString(self):
        return str(self.tiles)
    
    def getCount(self):
        sum = 0
        for numColor in self.tiles:
            sum += numColor
        return sum
    
    def getCountOfColor(self, color: TileColor):
        return self.tiles[self.getColorIndex(color)]
    
    def pickRandomTiles(self, count, rand):
        retTiles = TileCollection(0, 0, 0, 0, 0, 0)
        for _ in range(count):
            index = rand.random() * self.getCount()
            if index < self.tiles[0]:
                color = TileColor.BLUE
            elif index < self.tiles[0] + self.tiles[1]:
                color = TileColor.YELLOW
            elif index < self.tiles[0] + self.tiles[1] + self.tiles[2]:
                color = TileColor.RED
            elif index < self.tiles[0] + self.tiles[1] + self.tiles[2] + self.tiles[3]:
                color = TileColor.BLACK
            elif index < self.tiles[0] + self.tiles[1] + self.tiles[2] + self.tiles[3] + self.tiles[4]:
                color = TileColor.CYAN
            else:
                color = TileColor.WHITE
            self.removeTiles(color, 1)
            retTiles.addTiles(color, 1)
        
        return retTiles

    def addTiles(self, color, count):
        index = TileCollection.getColorIndex(color)
        self.tiles[index] += count

    def removeTiles(self, color, count):
        index = TileCollection.getColorIndex(color)
        self.tiles[index] -= count
        if self.tiles[index] < 0:
            print("Removed tiles that didn't exist: ", color, count)
            exit(0)
    
    def moveAllTiles(self, location):
        for color in TileColor:
            count = self.getCountOfColor(color)
            location.addTiles(color, count)
            self.removeTiles(color, count)
    
    def getArray(self):
        return np.array(self.tiles)
    
    @staticmethod
    def getFromArray(arr):
        return TileCollection(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])