import sys

sys.path.append('..')
from Game import Game
from .AzulLogic import Board
import random

class AzulGame(Game):

    def __init__(self):
        self.rand = random.Random()

    def getInitBoard(self):
        board = Board().convertToArray()
        return board

    def getBoardSize(self):
        return (24, 6)

    def getActionSize(self):
        numActionableColors = 5 # Blue, Yellow, Red, Black, Cyan
        numTileLocations = 6    # 5 factories, 1 center
        numPlayerRows = 6       # 5 pattern lines, 1 floor line

        return numActionableColors * numTileLocations * numPlayerRows

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
        boardObj = Board.convertFromArray(board)
        newBoard = boardObj.getNextState(player, action)
        return (newBoard.convertToArray(), -player)

    def getValidMoves(self, board: Board, player: int):
        """
        Input:
            board: current board
            player: current player
        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves
        """
        boardObj = Board.convertFromArray(board)
        moves = []
        for i in range(180):
            action = boardObj.decodeAction(player, i)
            moves.append(1) if boardObj.isActionValid(action) else moves.append(0)

        return moves

    def getGameEnded(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)
        Returns:
            r: 0 if game has not ended. 1 if player won, -1 if player lost,
               small non-zero value for draw.
               
        """
        boardObj = Board.convertFromArray(board)
        if boardObj.roundFinished:
            if player == 1:
                curPlayer = boardObj.player1
                otherPlayer = boardObj.player2
            else:
                curPlayer = boardObj.player2
                otherPlayer = boardObj.player1
            
            if curPlayer.score > otherPlayer.score:
                return 1
            elif otherPlayer.score > curPlayer.score:
                return -1
            else:
                return .000001
        else:
            return 0

    def getCanonicalForm(self, board, player):
        """
        Input:
            board: current board
            player: current player (1 or -1)
        Returns:
            canonicalBoard: returns canonical form of board. The canonical form
                            should be independent of player. For e.g. in chess,
                            the canonical form can be chosen to be from the pov
                            of white. When the player is white, we can return
                            board as is. When the player is black, we can invert
                            the colors and return the board.
        """
        return board

    def stringRepresentation(self, board):
        """
        Input:
            board: current board
        Returns:
            boardString: a quick conversion of board to a string format.
                         Required by MCTS for hashing.
        """
        return str(board)
    
    def getSymmetries(self, board, pi):
        """
        Input:
            board: current board
            pi: policy vector of size self.getActionSize()

        Returns:
            symmForms: a list of [(board,pi)] where each tuple is a symmetrical
                       form of the board and the corresponding pi vector. This
                       is used when training the neural network from examples.
        """
        # Azul has no symmetries :(
        return [(board, pi)]

    @staticmethod
    def display(board):
        print(board)
    
