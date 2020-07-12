from .Player import Player

class Board():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def display(self):
        self.player1.display()
        print()
        self.player2.display()

