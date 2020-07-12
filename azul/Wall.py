class Wall:
    def __init__(self):
        self.cells = [None] * 5
        for i in range(5):
            self.cells[i] = [False] * 5
    
    def display(self):
        print("WALL:")
        for i in range(5):
            line = ""
            for j in range(5):
                line += str(self.cells[i][j]) + ","
            print(line)
    

                