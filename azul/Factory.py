from .TileCollection import TileCollection

class Factory():
    def __init__(self, bag):
        self.tiles = bag.pickRandomTiles(4)
    
    def toString(self):
        return self.tiles.toString()
