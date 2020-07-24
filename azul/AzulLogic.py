from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .Bag import Bag
from .TileColor import TileColor
from .AzulAction import AzulAction
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

        return AzulAction(retPlayer, location, TileColor(color), line)
    
    def isActionValid(self, action: AzulAction):
        # Quit if source/color combo doesn't exist in center.
        if self.center.countTiles(action.source, action.color) == 0:
            return False

        # Quit if line is full or is already of another color 
        if not action.player.playerLines.isActionValid(action.color, action.line):
            return False
        
        # Quit if the wall tile associated with the line/color is filled
        if action.line != 5 and action.player.wall.isCellFilled(action.line, action.color):
            return False
        
        return True
    
    def executeAction(self, action):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action)
            exit(2)

        # Manipulate tiles from center
        tilesInHand = self.center.takeTiles(action)

        # Place tiles on player board
        overflow = action.player.placeTilesFromAction(action, tilesInHand)

        # Potentially put overflow in lid

        return self
        



