class TileCollection():
    def __init__(self, numBlue, numYellow, numRed, numBlack, numCyan, numWhite):
        self.tiles = [numBlue, numYellow, numRed, numBlack, numCyan, numWhite]

    def display(self):
        print("BAG:")
        print(self.tiles)