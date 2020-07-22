from .TileColor import TileColor

class PlayerLines():
    def __init__(self):
        self.lines = []
        self.lines.append((1, None, 0))
        self.lines.append((2, None, 0))
        self.lines.append((3, None, 0))
        self.lines.append((4, None, 0))
        self.lines.append((5, None, 0))
    
    def display(self):
        print(self.toString())
    
    def toString(self):
        string = "PLAYER LINES:\n"
        for line in self.lines:
            string += (str(line) + "\n")
        return string
    
    def isActionValid(self, color, line):
        if line != 5 and self.lines[line][0] == self.lines[line][2]:
            return False
        
        if line != 5 and self.lines[line][1] != None and color != self.lines[line][1]:
            return False
        
        return True