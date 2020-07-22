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

        #self.assertEqual(board.decodeAction(1, 13), (0, TileColor.RED, 1))
        #self.assertEqual(board.decodeAction(1, 0), (0, TileColor.BLUE, 0))
        #self.assertEqual(board.decodeAction(1, 1), (0, TileColor.BLUE, 1))
        #self.assertEqual(board.decodeAction(1, 121), (4, TileColor.BLUE, 1))
    
    def test_actionValid(self):
        game = AzulGame()
        board = Board()
        board.display()

        for i in range(180):
            action = board.decodeAction(1, i)
            print(i, action, board.isActionValid(action))
        
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()



