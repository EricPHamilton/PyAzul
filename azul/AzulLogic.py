from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .Bag import Bag
import random

class Board():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.bag = Bag()
        self.center = Center(self.bag)

    def display(self):
        self.bag.display()
        print()
        self.center.display()
        print()
        self.player1.display()
        print()
        self.player2.display()


