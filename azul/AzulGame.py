import sys

sys.path.append('..')
from Game import Game
from .AzulLogic import AzulBoard
from .TileCollection import TileCollection
from .BoardConverter import BoardConverter
from .AzulAction import AzulAction
from .Wall import Wall
import random
import numpy as np
import itertools

class AzulGame(Game):

    def __init__(self, shouldRandomize: bool):
        self.shouldRandomize = shouldRandomize

    def getInitBoard(self):
        boardObj = AzulBoard()
        if self.shouldRandomize:
            boardObj.fillWallsRandomly(random.uniform(0, 0.75))
            tilesOnPlayerWalls = TileCollection()
            tilesOnPlayerWalls.addTilesFromCollection(boardObj.player1.wall.getAllTiles())
            tilesOnPlayerWalls.addTilesFromCollection(boardObj.player2.wall.getAllTiles())
            boardObj.bag.removeTilesFromCollection(tilesOnPlayerWalls)

            boardObj.fillPlayerLinesRandomly(boardObj.bag, random.uniform(0, 0.5))
        
            allTiles = boardObj.getAllTiles()
            if not allTiles.equals(TileCollection(20, 20, 20, 20, 20, 1)):
                print ("Tile Randomization failed.")
                system.exit(3)
            
        board = BoardConverter.createArrayFromBoard(boardObj)
        return board

    def getBoardSize(self):
        return (25, 6)

    def getActionSize(self):
        #numActionableColors = 5  ==> Blue, Yellow, Red, Black, Cyan
        #numTileLocations = 6     ==> 5 factories, 1 center
        #numPlayerRows = 6        ==> 5 pattern lines, 1 floor line

        return 180 # numActionableColors * numTileLocations * numPlayerRows

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
        boardObj = BoardConverter.createBoardFromArray(board)
        newBoard = boardObj.getNextState(player, action)
        return (BoardConverter.createArrayFromBoard(newBoard), -player)

    def getValidMoves(self, board, player: int):
        """
        Input:
            board: current board
            player: current player
        Returns:
            validMoves: a binary vector of length self.getActionSize(), 1 for
                        moves that are valid from the current board and player,
                        0 for invalid moves
        """
        moves = [0] * self.getActionSize()
        for i in range(self.getActionSize()):
            action = AzulAction.getActionFromInt(i, player)

            playerArr = BoardConverter.getPlayerArray(board, player)
            centerArr = BoardConverter.getCenterArray(board)

            # Quit if source/color combo doesn't exist in center.
            if centerArr[action.source][action.color.value] == 0:
                continue

            if action.dest != 5:
                colorOfLine = playerArr[0][action.dest + 1]
                countOfLine = playerArr[1][action.dest + 1]
                # We're not good if the color of line is not empty AND not equal to action.
                if colorOfLine != -1 and colorOfLine != action.color.value:
                    continue

                # We're not good if the line is full.
                if countOfLine >= action.dest + 1:
                    continue
                    
                # Quit if the wall tile associated with the line/color is filled
                if playerArr[3 + action.dest][Wall.getIndexOfColorInRow(action.dest, action.color)] == 1:
                    continue

            moves[i] = 1
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
        boardObj = BoardConverter.createBoardFromArray(board)
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
        # basically just swap the player rows if player == -1
        if player == -1:
            arr = np.zeros((25, 6))
            for i in range(8):
                arr[i] = board[i]
            for i in range(8):
                arr[i + 8] = board[i + 16]
            for i in range(8):
                arr[i + 16] = board[i + 8]
            arr[24] = board[24]
            return arr
        else:
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

        # Only symmetries are ALL permutations of the factory rows.
        
        syms = [(board, pi)]
        evalSyms = False #setting to false because it might be broken
        if evalSyms:
            perms = list(itertools.permutations([0, 1, 2, 3, 4]))
            perms.pop(0) # current board
            
            indivLines = []
            indivPolicies = []
            for i in range(5):
                indivLines.append(board[i])
            
            for i in range(6):
                startInd = i * 30
                indivPolicies.append(pi[startInd:startInd+30])
            

            for perm in list(perms):
                newBoard = board.copy()
                newPi = []
                for i in range(5):
                    newBoard[i] = indivLines[perm[i]]
                    newPi.extend(indivPolicies[perm[i]])
                newPi.extend(indivPolicies[5])
                syms.append((newBoard, newPi))

        return syms

    @staticmethod
    def display(board):
        boardObj = BoardConverter.createBoardFromArray(board)
        boardObj.display()
    
