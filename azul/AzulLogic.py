from .Player import Player
from .TileCollection import TileCollection
from .Center import Center
from .Bag import Bag
from .TileColor import TileColor
from .AzulAction import AzulAction
import random
import numpy as np

class Board():
    def __init__(self):
        self.player1 = Player(1)
        self.player2 = Player(-1)
        self.bag = Bag()
        self.center = Center(self.bag)
        self.lid = TileCollection(0, 0, 0, 0, 0, 0)
        self.roundFinished = False

    def display(self):
        print("---------------------------------------------------------")
        #self.bag.display()
        #self.lid.display()
        #print()
        self.center.display()
        print()
        self.player1.display()
        print()
        self.player2.display()
        print("---------------------------------------------------------")
    
    def toString(self):
        return self.bag.toString() + self.lid.toString() + self.center.toString() + self.player1.toString() + self.player2.toString()

    def getNextState(self, player, actionInt):
        action = self.decodeAction(player, actionInt)
        return self.executeAction(action)
    
    def decodeAction(self, player: int, actionInt):
        location = actionInt // 30
        color = (actionInt % 30) // 6
        line = (actionInt % 30) % 6

        return AzulAction(player, location, TileColor(color), line)
    
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
    
    def executeAction(self, action: AzulAction):
        if not self.isActionValid(action):
            print("Attempted to execute an invalid action! Quitting with action:", action.toString())
            #print("actionColor:", action.color, "lineColor:", self.getPlayerFromAction(action).playerLines.lines[action.line][1])
            #action.playerID = -action.playerID
            #print("Swap player:", self.isActionValid(action))
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
        tilesToBag.moveAllTiles(self.bag.tiles)
        
        tilesToBag = self.player2.finishRound()
        self.player2.floorLine.tileCollection.moveAllTiles(self.lid)
        tilesToBag.moveAllTiles(self.bag.tiles)

        #print("Player 1 wall:", str(self.player1.score), "points.")
        #print(self.player1.wall.toString())
        #print("Player 2 wall:", str(self.player2.score), "points.")
        #print(self.player2.wall.toString())
        #TODO need to indicate that player w/ white tile goes first
    
    # This will be ugly... We need to convert the entirety of the board into an array. Yikes.
    def convertToArray(self):
        arr = np.zeros((25, 6))
        for i in range(5):
            arr[i] = self.center.factories[i].tiles.getArray()
        arr[5] = self.center.center.getArray()
        arr[6] = self.bag.tiles.getArray()
        arr[7] = self.lid.getArray()

        player1Arr = self.player1.getArray()
        for i in range(8):
            arr[8 + i] = player1Arr[i]

        player2Arr = self.player2.getArray()
        for i in range(8):
            arr[16 + i] = player2Arr[i]
        
        arr[24][0] = int(self.roundFinished)
        for i in range(5):
            arr[24][i + 1] = -2

        '''board2 = Board.convertFromArray(arr)
        if self.toString() != board2.toString():
            print("There was a mistake converting from board -> arr")
            exit(-2)'''

        return arr
    
    # More ugly. Now we need to create board given the array output from convertToArray...
    @staticmethod
    def convertFromArray(arr):
        arr = arr.astype(int)
        retBoard = Board()
        for i in range(5):
            retBoard.center.factories[i].tiles = TileCollection.getFromArray(arr[i])
        retBoard.center.center = TileCollection.getFromArray(arr[5])
        retBoard.bag.tiles = TileCollection.getFromArray(arr[6])
        retBoard.lid = TileCollection.getFromArray(arr[7])
        retBoard.player1 = Player.getFromArray(arr[8:16])
        retBoard.player2 = Player.getFromArray(arr[16:24])
        retBoard.roundFinished = bool(arr[24][0])

        '''arr2 = retBoard.convertToArray()
        if not np.array_equal(arr, arr2):
            print("There was a mistake converting from arr -> board")
            exit(-2)
        '''

        return retBoard

        