from .Wall import Wall
from .FloorLine import FloorLine
from .PlayerLines import PlayerLines

class Player:
    def __init__(self):
        self.wall = Wall()
        self.floorLine = FloorLine()
        self.playerLines = PlayerLines()
    
    def display(self):
        self.playerLines.display()
        self.wall.display()
        self.floorLine.display()