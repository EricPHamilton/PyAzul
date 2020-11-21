from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .TileColor import TileColor
from .AzulAction import AzulAction
import random
import numpy as np
import math

class AzulBoard():
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(-1)
        self.bag = TileCollection(20, 20, 20, 20, 20, 0)
        self.lid = TileCollection()
        self.center = Center(self.bag, self.lid)
        self.roundFinished = False
        self.playerIDWhoHadWhiteLastRound = 0

    def display(self):
        print("---------------------------------------------------------")
        print("Bag:", self.bag.toString())
        self.lid.display()
        
        self.center.display()
        print()
        self.player1.display()
        print()
        self.player2.display()
        print("---------------------------------------------------------")
    
    def toString(self):
        return self.bag.toString() + self.lid.toString() + self.center.toString() + self.player1.toString() + self.player2.toString()

    def fillWallsRandomly(self, prob: float):
        self.player1.wall.cells = self.getValidRandomWall(prob)
        self.player2.wall.cells = self.getValidRandomWall(prob)
    
    def getValidRandomWall(self, prob: float):
        valid = False
        while not valid:
            numpyWall = np.random.choice(a=[True, False], size=(5, 5), p = [prob, 1-prob])
            valid = True
            for line in numpyWall:
                if line.all():
                    valid = False
            
        return numpyWall.tolist()
    
    def fillPlayerLinesRandomly(self, bag, lineHasTilesProb: float):
        self.player1.playerLines.lines = self.getValidRandomPlayerLines(bag, self.player1, lineHasTilesProb)
        self.player2.playerLines.lines = self.getValidRandomPlayerLines(bag, self.player2, lineHasTilesProb)

    def getValidRandomPlayerLines(self, bag, player, lineHasTilesProb: float):
        lines = []
        for i in range(5):
            addSomeTiles = np.random.uniform(0, 1) < lineHasTilesProb
            if addSomeTiles:
                validColors = player.wall.getValidColorsForRow(i)
                color = np.random.choice(validColors)
                number = min(np.random.randint(0, i + 1), bag.getCountOfColor(color)) # Don't remove tiles we don't have in the bag.
                if number == 0:
                    color = None
                else:
                    bag.removeTiles(color, number)
            else:
                color = None
                number = 0

            lines.append([i + 1, color, number])
        
        return lines


    def getNextState(self, player, actionInt):
        action = AzulAction.getActionFromInt(actionInt, player)
        return self.executeAction(action)
    
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
        if not actionPlayer.playerLines.isActionValid(action.color, action.dest):
            return False
        
        # Quit if the wall tile associated with the line/color is filled
        if action.dest != 5 and actionPlayer.wall.isCellFilled(action.dest, action.color):
            return False
        
        return True
    
    def executeAction(self, action: AzulAction):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action.toString())
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
        self.playerIDWhoHadWhiteLastRound = 0 # Reset 

        # Track if player1 had white tile
        if (self.player1.floorLine.tileCollection.getCountOfColor(TileColor.WHITE) > 0):
            self.playerIDWhoHadWhiteLastRound = self.player1.id

        # move tiles to bag and lid
        (tilesToBag, tilesToLid) = self.player1.finishRound()
        tilesToBag.moveAllTiles(self.bag)
        tilesToLid.moveAllTiles(self.lid)

        if (self.player2.floorLine.tileCollection.getCountOfColor(TileColor.WHITE) > 0):
            self.playerIDWhoHadWhiteLastRound = self.player2.id

        (tilesToBag, tilesToLid) = self.player2.finishRound()
        tilesToBag.moveAllTiles(self.bag)
        tilesToLid.moveAllTiles(self.lid)

    
    def setupNextRound(self):
        self.roundFinished = False
        self.center = Center(self.bag, self.lid)

    def isGameFinished(self):
        return self.player1.wall.hasFinishedRow() or self.player2.wall.hasFinishedRow()
    
    def getAllTiles(self):
        # Created as a sanity check. Make sure there are 20/20/20/20/20/1 tiles in the game at all times.

        sumTiles = TileCollection()
        sumTiles.addTilesFromCollection(self.bag)
        sumTiles.addTilesFromCollection(self.lid)
        sumTiles.addTilesFromCollection(self.player1.getAllTiles())
        sumTiles.addTilesFromCollection(self.player2.getAllTiles())
        sumTiles.addTilesFromCollection(self.center.getAllTiles())

        return sumTiles        