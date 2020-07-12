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
        print("PLAYER LINES:")
        for line in self.lines:
            print(line)