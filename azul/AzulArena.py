import logging

from tqdm import tqdm
from .AzulLogic import AzulBoard
from .TileCollection import TileCollection
from .BoardConverter import BoardConverter

log = logging.getLogger(__name__)

class AzulArena():
    """
    An Arena class where any 2 agents can be pit against each other.
    """

    def __init__(self, player1, player2, game, display=None):
        """
        Input:
            player 1,2: two functions that takes board as input, return action
            game: Game object
            display: a function that takes board as input and prints it (e.g.
                     display in othello/OthelloGame). Is necessary for verbose
                     mode.

        see othello/OthelloPlayers.py for an example. See pit.py for pitting
        human players/other baselines with each other.
        """
        self.player1 = player1
        self.player2 = player2
        self.game = game
        self.display = display

    def playRound(self, board, verbose=False) -> AzulBoard:
        """
        Executes one episode of a game.

        Returns:
            either
                winner: player who won the game (1 if player1, -1 if player2)
            or
                draw result returned from the game that is neither 1, -1, nor 0.
        """
        players = [self.player2, None, self.player1]
        curPlayer = BoardConverter.createBoardFromArray(board).playerIDWhoHadWhiteLastRound
        if curPlayer == 0:
            curPlayer = 1
            
        it = 0
        while self.game.getGameEnded(board, curPlayer) == 0:
            it += 1
            if verbose:
                assert self.display
                print("Turn ", str(it), "Player ", str(curPlayer))
                self.display(board)
            action = players[curPlayer + 1](self.game.getCanonicalForm(board, curPlayer))

            valids = self.game.getValidMoves(self.game.getCanonicalForm(board, curPlayer), 1)

            if valids[action] == 0:
                log.error(f'Action {action} is not valid!')
                log.debug(f'valids = {valids}')
                assert valids[action] > 0
            board, curPlayer = self.game.getNextState(board, curPlayer, action)
            if verbose:
                tempBoard = AzulBoard()
                actionObj = tempBoard.decodeAction(curPlayer, action)
                print(actionObj.getTurnExplanationString())
        if verbose:
            assert self.display
            print("Round over: Turn ", str(it), "Result ", str(self.game.getGameEnded(board, 1)))
            self.display(board)
        
        retBoard = BoardConverter.createBoardFromArray(board)
        if  retBoard.getAllTiles().equals(TileCollection(20, 20, 20, 20, 20, 1)):
            print("Gained or lost a tile somewhere!")
            exit(-3)

        return BoardConverter.createBoardFromArray(board)

    def playFullGame(self, verbose=False):
        """
        Plays a full game of Azul, comprised of many rounds.

        Returns:
            oneWon: games won by player1
            twoWon: games won by player2
            draws:  games won by nobody
        """
        board = None
        gameIsFinished = False

        while not gameIsFinished:
            if board is None:
                board = self.game.getInitBoard()
            else:
                boardObj = BoardConverter.createBoardFromArray(board)
                boardObj.setupNextRound()
                board = BoardConverter.createArrayFromBoard(boardObj)

            newBoard = self.playRound(board, verbose=verbose)
            gameIsFinished = newBoard.isGameFinished()
            board = BoardConverter.createArrayFromBoard(newBoard)


