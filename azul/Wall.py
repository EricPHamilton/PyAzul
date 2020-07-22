from .TileColor import TileColor

class Wall:
    def __init__(self):
        self.cells = [[False] * 5 for i in range(5)]
    
    def display(self):
        print("WALL:")
        print(self.toString())
    
    def toString(self):
        for i in range(5):
            line = ""
            for j in range(5):
                line += str(int(self.cells[i][j])) + ","
            line += "\n"
        return line

    @staticmethod
    def getColorGrid():
        return [
            [TileColor.BLUE, TileColor.YELLOW, TileColor.RED, TileColor.BLACK, TileColor.CYAN],
            [TileColor.CYAN, TileColor.BLUE, TileColor.YELLOW, TileColor.RED, TileColor.BLACK],
            [TileColor.BLACK, TileColor.CYAN, TileColor.BLUE, TileColor.YELLOW, TileColor.RED],
            [TileColor.RED, TileColor.BLACK, TileColor.CYAN, TileColor.BLUE, TileColor.YELLOW],
            [TileColor.YELLOW, TileColor.RED, TileColor.BLACK, TileColor.CYAN, TileColor.BLUE]
        ]

    @staticmethod
    def getIndexOfColorInRow(rowIndex, color):
        colors = Wall.getColorGrid()
        row = colors[rowIndex]
        for i in range(len(row)):
            if row[i] == color:
                return i
        
        return None
    
    def isCellFilled(self, line, color):
        return self.cells[line][Wall.getIndexOfColorInRow(line, color)]
    

                