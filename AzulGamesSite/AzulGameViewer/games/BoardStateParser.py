class BoardStateParser:
    def getFactories(self, boardState):
        factories = []
        for i in range(5):
            factories.append(boardState[i])
        return factories
    
    def getBag(self, boardState):
        return boardState[5]
    
    def getLid(self, boardState):
        return boardState[6]
    
    def getPlayer(self, boardState, playerID):
        playerDict = {}

        if playerID == 1:
            startingRow = 8
        else:
            startingRow = 16
        
        playerDict['id'] = boardState[startingRow][0]
        playerDict['score'] = boardState[startingRow + 1][0]
        
        playerLines = []
        for i in range(5):
            color = boardState[startingRow][i + 1]
            number = boardState[startingRow + 1][i + 1]
        playerLines.append([color, number])

        playerDict['playerLines'] = playerLines
        playerDict['floorLine'] = boardState[startingRow + 2]

        wall = []
        for i in range(5):
            wall.append(boardState[startingRow + 3][:-1])
        
        playerDict['wall'] = wall

        return playerDict

    def getBoardContextVars(self, boardState):
        retDict = {}

        retDict['board_state'] = boardState
        retDict['factories'] = self.getFactories(boardState)
        retDict['bag'] = self.getBag(boardState)
        retDict['lid'] = self.getLid(boardState)
        retDict['player1'] = self.getPlayer(boardState, 1)
        retDict['player2'] = self.getPlayer(boardState, -1)
        
        return retDict
