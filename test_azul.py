from azul.AzulGame import AzulGame
from azul.AzulLogic import Board
from azul.TileColor import TileColor
from azul.AzulAction import AzulAction
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
            print(i, action.toString(), board.isActionValid(action))
        
        self.assertEqual(1, 1)

if __name__ == "__main__":
    #unittest.main()

    game = AzulGame()
    board = game.getInitBoard()
    playerInt = 1

    while True:
        board.display()
        if playerInt == 1:
            player = board.player1
        else:
            player = board.player2

        source = int(input("Source input (0 - 5):"))
        color = int(input("Color input (0 - 4):"))
        line = int(input("Line input (0 - 5):"))
        action = AzulAction(player, source, TileColor(color), line)
        actionInt = action.getActionInt()
        print(str(action.getActionInt()))
        board, playerInt = game.getNextState(board, playerInt, actionInt)




