from azul.AzulGame import AzulGame
from azul.AzulLogic import Board
import unittest

class AzulTests(unittest.TestCase):
    def test_board(self):
        game = AzulGame()
        board = Board()
        self.assertEqual(board.player1.floorLine.getCount(), 0)

if __name__ == "__main__":
    game = AzulGame()
    game.display(Board())
    unittest.main()



