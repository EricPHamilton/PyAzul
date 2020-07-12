from .TileColor import TileColor

class PlayerLines():
    def __init__(self):
        self.lines = []
        self.lines.append((1, TileColor.BLUE, 0))
        self.lines.append((2, TileColor.YELLOW, 0))
        self.lines.append((3, TileColor.RED, 0))
        self.lines.append((4, TileColor.BLACK, 0))
        self.lines.append((5, TileColor.CYAN, 0))
    
    def display(self):
        print("PLAYER LINES:")
        for line in self.lines:
            print(line)