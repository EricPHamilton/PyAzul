from .TileCollection import TileCollection
from .TileColor import TileColor
import random

class Bag():
    def __init__(self):
        self.tiles = TileCollection(20, 20, 20, 20, 20, 0)
        self.rand = random.Random()
            
    def pickRandomTiles(self, count):
        return self.tiles.pickRandomTiles(4, self.rand)

    def display(self):
        print(self.toString())
    
    def toString(self):
        return "Bag: " + self.tiles.toString()
