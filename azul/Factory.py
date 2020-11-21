from .TileCollection import TileCollection

class Factory():
    def __init__(self, bag: TileCollection, lid: TileCollection):
        if bag.getCount() >= 4:
            self.tiles = bag.pickRandomTiles(4)
        else:
            self.tiles = TileCollection()
            # Move all tiles that are left in the bag
            bag.moveAllTiles(self.tiles)
            numberStillNeeded = 4 - self.tiles.getCount()

            # Move all tiles from lid to the bag
            lid.moveAllTiles(bag)

            # Note: Azul rules state that if after taking from the lid, we *still* don't
            # have enough tiles, we continue even though all factory displays are not filled.
            # This condition is impossible to hit in 2-player Azul, which is why I haven't
            # implemented it.

            # continue randomly picking
            remainingTiles = bag.pickRandomTiles(numberStillNeeded)
            self.tiles.addTilesFromCollection(remainingTiles)
    
    def toString(self):
        return self.tiles.toString()
