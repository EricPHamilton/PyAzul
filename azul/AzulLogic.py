from .Player import Player
from .TileCollection import TileCollection

class Board():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.bag = TileCollection(20, 20, 20, 20, 20, 0)

    def display(self):
        self.bag.display()
        print()
        self.player1.display()
        print()
        self.player2.display()

