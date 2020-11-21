from .AzulLogic import AzulBoard
from .TileCollection import TileCollection
from .Player import Player
import numpy as np


class BoardConverter:
    # This will be ugly... We need to convert the entirety of the board into an array. Yikes.
    def createArrayFromBoard(board: AzulBoard):
        arr = np.zeros((25, 6))
        for i in range(5):
            arr[i] = board.center.factories[i].tiles.getArray()
        arr[5] = board.center.center.getArray()
        arr[6] = board.bag.getArray()
        arr[7] = board.lid.getArray()

        player1Arr = board.player1.getArray()
        for i in range(8):
            arr[8 + i] = player1Arr[i]

        player2Arr = board.player2.getArray()
        for i in range(8):
            arr[16 + i] = player2Arr[i]
        
        arr[24][0] = int(board.roundFinished)
        arr[24][1] = board.playerIDWhoHadWhiteLastRound
        for i in range(4):
            arr[24][i + 2] = -2

        return arr
    
    # More ugly. Now we need to create board given the array output from createArrayFromBoard...
    @staticmethod
    def createBoardFromArray(arr):
        arr = arr.astype(int)
        retBoard = AzulBoard()
        for i in range(5):
            retBoard.center.factories[i].tiles = TileCollection.getFromArray(arr[i])
        retBoard.center.center = TileCollection.getFromArray(arr[5])
        retBoard.bag = TileCollection.getFromArray(arr[6])
        retBoard.lid = TileCollection.getFromArray(arr[7])
        retBoard.player1 = Player.getFromArray(arr[8:16])
        retBoard.player2 = Player.getFromArray(arr[16:24])
        retBoard.roundFinished = bool(arr[24][0])
        retBoard.playerIDWhoHadWhiteLastRound = int(arr[24][1])

        return retBoard
        