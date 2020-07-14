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
        action = self.decodeAction(player, actionInt)
        return self.executeAction(action)
    
    def decodeAction(self, player, actionInt):
        if player == 1:
            return self.player1
        else:
            return self.player2
        
        location = actionInt // 30
        color = (actionInt % 30) // 6 + 1 # Enum is 1-indexed
        line = (actionInt  % 30) % 6

        return (player, location, TileColor(color), line)
    
    def executeAction(self, action):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action)
            exit(2)

        return self

    def isActionValid(self, action):
        player, source, color, line = action
        
        # Quit if source/color combo doesn't exist in center.
        if not self.center.hasTiles(source, color):
            return False

        # Quit if line is full or is already of another color 
        if not player.playerLines.isActionValid(color, line):
            return False
        
        # Quit if the wall tile associated with the line/color is filled
        


