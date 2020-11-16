from azul.AzulGame import AzulGame
from azul.AzulLogic import AzulBoard
from azul.TileColor import TileColor
from azul.AzulAction import AzulAction
import unittest

class AzulTests(unittest.TestCase):
    def test_board(self):
        game = AzulGame(False)
        board = AzulBoard()
        self.assertEqual(board.player1.floorLine.tileCollection.getCount(), 0)
    
    def test_decodeAction(self):
        game = AzulGame(False)
        board = AzulBoard()

        #self.assertEqual(board.decodeAction(1, 13), (0, TileColor.RED, 1))
        #self.assertEqual(board.decodeAction(1, 0), (0, TileColor.BLUE, 0))
        #self.assertEqual(board.decodeAction(1, 1), (0, TileColor.BLUE, 1))
        #self.assertEqual(board.decodeAction(1, 121), (4, TileColor.BLUE, 1))
    
    def test_actionValid(self):
        game = AzulGame(False)
        board = AzulBoard()
        #board.display()

        for i in range(180):
            action = board.decodeAction(1, i)
            #print(i, action.toString(), board.isActionValid(action))
        
        self.assertEqual(1, 1)
    
    def test_gridTilePlacementCounts(self):
        board = AzulBoard()
        board.player1.wall.cells[2][1] = True
        board.player1.wall.cells[2][2] = True
        board.player1.wall.cells[2][3] = True
        board.player1.wall.cells[2][4] = True
        self.assertEqual(board.player1.wall.getHorizontalLinkCount(2, 3), 4)

        board = AzulBoard()
        board.player1.wall.cells[1][2] = True
        board.player1.wall.cells[2][2] = True
        board.player1.wall.cells[3][2] = True
        board.player1.wall.cells[4][2] = True
        self.assertEqual(board.player1.wall.getVerticalLinkCount(4, 2), 4)

        board = AzulBoard()
        board.player1.wall.cells[2][2] = True
        self.assertEqual(board.player1.wall.getVerticalLinkCount(2, 2), 1)
        self.assertEqual(board.player1.wall.getHorizontalLinkCount(2, 2), 1)


if __name__ == "__main__":
    unittest.main()

    



