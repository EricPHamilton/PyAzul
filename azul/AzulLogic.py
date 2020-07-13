from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .Bag import Bag
from .TileColor import TileColor
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

    def getNextState(self, player, actionInt):
        action = self.decodeAction(actionInt)
        return self.executeAction(action)
    
    def decodeAction(self, actionInt):
        location = actionInt // 30
        color = (actionInt % 30) // 6 + 1 # Enum is 1-indexed
        line = (actionInt  % 30) % 6

        return (location, TileColor(color), line)
    
    def executeAction(self, action):
        return self


