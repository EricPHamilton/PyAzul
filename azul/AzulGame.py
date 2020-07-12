import sys

sys.path.append('..')
from Game import Game
from .AzulLogic import Board

class AzulGame(Game):
    @staticmethod
    def display(board):
        board.display()