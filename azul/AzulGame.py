import sys

sys.path.append('..')
from Game import Game
from .AzulLogic import Board
import random

class AzulGame(Game):

    def __init__(self):
        self.rand = random.Random()

    def getInitBoard(self):
        board = Board()
        return None

    def getBoardSize(self):
        return (6, 6)

    def getActionSize(self):
        numActionableColors = 5 # Blue, Yellow, Red, Black, Cyan
        numTileLocations = 6    # 5 factories, 1 center
        numPlayerRows = 6       # 5 pattern lines, 1 floor line

        return (numActionableColors * numTileLocations * numPlayerRows)

    def getNextState(self, board, player, action):
        """
        Input:
            board: current board
            player: current player (1 or -1)
            action: action taken by current player
        Returns:
            nextBoard: board after applying action
            nextPlayer: player who plays in the next turn (should be -player)
        """
        # will need to check for white tile at end of rounds
        return (board.getNextState(player, action), -player)

    def getValidMoves(self, board, player):
        """
        Input:
            board: current board
            player: current player
        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves
        """
        pass

    def getGameEnded(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)
        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.
               
        """
        pass

    def stringRepresentation(self, board):
        """
        Input:
            board: current board
        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.
        """
        return board.toString()

    @staticmethod
    def display(board):
        board.display()
    
