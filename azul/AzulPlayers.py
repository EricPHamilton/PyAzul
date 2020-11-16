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
        valid = self.game.getValidMoves(board, 1)

        while True:
            source = input("Take tiles from: ")
            if source == 'c':
                source = 5
            else:
                source = int(source) - 1
            
            color = int(input("Color: "))
            color = color - 1

            line = input("What line to place on: ")
            if line == 'f':
                line = 5
            else:
                line = int(line) - 1
            
            action = AzulAction(-1, source, TileColor(color), line)
            actionInt = action.getActionInt()

            if valid[actionInt] == 1:
                print("---------------------------------------------------------")
                return actionInt
            else:
                print("attempted invalid move. try again.")
        
        return None