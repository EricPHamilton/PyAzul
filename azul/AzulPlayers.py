import numpy as np
from .AzulAction import AzulAction
from .TileColor import TileColor

class RandomPlayer():
    def __init__(self, game):
        self.game = game
    
    def play(self, board):
        a = np.random.randint(self.game.getActionSize())
        valids = self.game.getValidMoves(board, 1)
        while valids[a] != 1:
            a = np.random.randint(self.game.getActionSize())
        return a

class HumanAzulPlayer():
    def __init__(self, game):
        self.game = game
    
    def play(self, board):
        valid = self.game.getValidMoves(board, -1)
        
        source = int(input("Source input (0 - 5):"))
        color = int(input("Color input (0=Blue, 1=Yellow):"))
        line = int(input("Line input (0 - 5):"))

        action = AzulAction(-1, source, TileColor(color), line)
        actionInt = action.getActionInt()

        if valid[actionInt] == 1:
            return actionInt
        else:
            print("attempted invalid move")
            quit(-2)
        
        return None