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
        self.lid = TileCollection(0, 0, 0, 0, 0, 0)
        self.roundFinished = False

    def display(self):
        self.bag.display()
        self.lid.display()
        print()
        self.center.display()
        print()
        self.player1.display()
        print()
        self.player2.display()
    
    def toString(self):
        self.bag.toString() + self.lid.toString() + self.center.toString() + self.player1.toString() + self.player2.toString()

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

        return AzulAction(retPlayer.id, location, TileColor(color), line)
    
    def getPlayerFromAction(self, action: AzulAction) -> Player:
        if action.playerID == 1:
            return self.player1
        else:
            return self.player2
    
    def isActionValid(self, action: AzulAction):
        actionPlayer = self.getPlayerFromAction(action)

        # Quit if source/color combo doesn't exist in center.
        if self.center.countTiles(action.source, action.color) == 0:
            return False

        # Quit if line is full or is already of another color 
        if not actionPlayer.playerLines.isActionValid(action.color, action.line):
            return False
        
        # Quit if the wall tile associated with the line/color is filled
        if action.line != 5 and actionPlayer.wall.isCellFilled(action.line, action.color):
            return False
        
        return True
    
    def executeAction(self, action):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action)
            exit(2)

        actionPlayer = self.getPlayerFromAction(action)
        
        # Manipulate tiles from center
        tilesInHand = self.center.takeTiles(action)

        # Place tiles on player board
        overflow = actionPlayer.placeTilesFromAction(action, tilesInHand)

        # Potentially put overflow in lid
        self.lid.addTiles(action.color, overflow.getCountOfColor(action.color))

        if self.shouldFinishRound():
            self.finishRound()

        return self
        
    def shouldFinishRound(self) -> bool:
        for factory in self.center.factories:
            if factory.tiles.getCount() > 0:
                return False
        
        if self.center.center.getCount() > 0:
            return False
        
        return True
    
    def finishRound(self):
        self.roundFinished = True

        tilesToBag = self.player1.finishRound()
        self.player1.floorLine.tileCollection.moveAllTiles(self.lid)
        
        tilesToBag = self.player2.finishRound()
        self.player2.floorLine.tileCollection.moveAllTiles(self.lid)

        #TODO need to indicate that player w/ white tile goes first