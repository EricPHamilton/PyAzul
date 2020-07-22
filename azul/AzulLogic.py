from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .Bag import Bag
from .TileColor import TileColor
import random

class Board():
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(-1)
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
    
    def toString(self):
        self.bag.toString() + self.center.toString() + self.player1.toString() + self.player2.toString()

    def getNextState(self, player, actionInt):
        action = self.decodeAction(player, actionInt)
        return self.executeAction(action)
    
    def decodeAction(self, player, actionInt):
        if player == 1:
            retPlayer = self.player1
        else:
            retPlayer = self.player2
        
        location = actionInt // 30
        color = (actionInt % 30) // 6
        line = (actionInt % 30) % 6

        return (retPlayer, location, TileColor(color), line)
    
    def executeAction(self, action):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action)
            exit(2)

        return self

    def isActionValid(self, action):
        player, source, color, line = action
        
        # Quit if source/color combo doesn't exist in center.
        if self.center.countTiles(source, color) == 0:
            return False

        # Quit if line is full or is already of another color 
        if not player.playerLines.isActionValid(color, line):
            return False
        
        # Quit if the wall tile associated with the line/color is filled
        if line != 5 and player.wall.isCellFilled(line, color):
            return False
        
        return True
        



