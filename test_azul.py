from azul.AzulGame import AzulGame
from azul.AzulLogic import Board
from azul.TileColor import TileColor
import unittest

class AzulTests(unittest.TestCase):
    def test_board(self):
        game = AzulGame()
        board = Board()
        self.assertEqual(board.player1.floorLine.getCount(), 0)
    
    def test_decodeAction(self):
        game = AzulGame()
        board = Board()

        self.assertEqual(board.decodeAction(13), (0, TileColor.RED, 1))
        self.assertEqual(board.decodeAction(0), (0, TileColor.BLUE, 0))
        self.assertEqual(board.decodeAction(1), (0, TileColor.BLUE, 1))
        self.assertEqual(board.decodeAction(121), (4, TileColor.BLUE, 1))

if __name__ == "__main__":
    game = AzulGame()
    game.display(Board())
    unittest.main()



