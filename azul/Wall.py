from .TileColor import TileColor
from .TileCollection import TileCollection

class Wall:
    def __init__(self):
        self.cells = [[False] * 5 for i in range(5)]
    
    def display(self):
        print("WALL:")
        print(self.toString())
    
    def toString(self):
        string = ""
        for i in range(5):
            line = ""
            for j in range(5):
                line += str(int(self.cells[i][j])) + ","
            line += "\n"
            string += line
        return string

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

    def getCountOfColor(self, color) -> int:
        ctr = 0
        for row in range(5):
            col = self.getIndexOfColorInRow(row, color)
            if self.cells[row][col] == True:
                ctr += 1
        
        return ctr

    def isColorComplete(self, color) -> bool:
        return self.getCountOfColor(color) == 5

    def getAllTiles(self) -> TileCollection:
        return TileCollection(self.getCountOfColor(TileColor.BLUE), self.getCountOfColor(TileColor.YELLOW), self.getCountOfColor(TileColor.RED), self.getCountOfColor(TileColor.BLUE), self.getCountOfColor(TileColor.CYAN), 0)

    # Returns scores from function getScoresForCell.
    def addTile(self, rowIndex, color) -> tuple:
        row = rowIndex
        col = self.getIndexOfColorInRow(row, color)
        self.cells[row][col] = True

        return self.getScoresForCell(row, col)

    # Returns two scores in a 2-cell array - [normalScore, bonusScore]
    # normal score is normal score for placing tile.
    # bonus score is points you're awarded at the end of the game (that we apply immediately so model prioritizes completing these)
    def getScoresForCell(self, row, col) -> tuple:
        normalScore = 0
        bonusScore = 0
        hori = self.getHorizontalLinkCount(row, col)
        vert = self.getVerticalLinkCount(row, col)        

        if hori == 1 and vert == 1: # Singleton tile. 1 pt.
            normalScore += 1
        elif hori == 1 or vert == 1: # Row/Col of tiles. X points 
            normalScore += (max(hori, vert))
        else:
            normalScore += (hori + vert) # cross of tiles. Hori + Vert points.
        
        if hori == 5: # Finished row. +2
            bonusScore += 2
        
        if vert == 5: # Finished col. +7
            bonusScore += 7
        
        if self.isColorComplete(self.getColorGrid()[row][col]): # Finished color. +10
            bonusScore += 10
        
        return (normalScore, bonusScore)

    def getHorizontalLinkCount(self, row, col) -> int:
        trackCol = col
        count = 0
        while trackCol > 0:
            if self.cells[row][trackCol - 1] == True:
                trackCol -= 1
            else:
                break
        
        while trackCol < 5:
            if self.cells[row][trackCol] == True:
                count += 1
                trackCol += 1
            else:
                break
        
        return count

    def getVerticalLinkCount(self, row, col) -> int:
        trackRow = row
        count = 0
        while trackRow > 0:
            if self.cells[trackRow - 1][col] == True:
                trackRow -= 1
            else:
                break
        
        while trackRow < 5:
            if self.cells[trackRow][col] == True:
                count += 1
                trackRow += 1
            else:
                break
        
        return count

    def isCellFilled(self, line, color):
        return self.cells[line][Wall.getIndexOfColorInRow(line, color)]
    
    def hasFinishedRow(self) -> bool:
        for i in range(5):
            onlyTrue = True
            for j in range(5):
                if self.cells[i][j] == False:
                    onlyTrue = False
            if onlyTrue:
                return True
        return False

                