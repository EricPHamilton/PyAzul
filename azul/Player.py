from .Wall import Wall
from .FloorLine import FloorLine
from .PlayerLines import PlayerLines

class Player:
    def __init__(self, id):
        self.id = id
        self.wall = Wall()
        self.floorLine = FloorLine()
        self.playerLines = PlayerLines()
    
    def toString(self):
        return str(self.id) + "\n" + self.playerLines.toString() + self.wall.toString() + self.floorLine.toString()
    
    def display(self):
        print(self.toString())