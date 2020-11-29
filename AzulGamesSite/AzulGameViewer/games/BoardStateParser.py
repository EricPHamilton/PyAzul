class BoardStateParser:
    def getColorCssClass(self, indexInTileCollection):
        if indexInTileCollection == 0:
            return "_tileBlue"
        elif indexInTileCollection == 1:
            return "_tileYellow"
        elif indexInTileCollection == 2:
            return "_tileRed"
        elif indexInTileCollection == 3:
            return "_tileBlack"
        elif indexInTileCollection == 4:
            return "_tileCyan"
        elif indexInTileCollection == 5:
            return "_tileWhite"
    
    def getWallColorCssClass(self, row, column):
        diff = column - row
        if diff < 0:
            diff = diff + 5
        return self.getColorCssClass(diff)

    def getTileLine(self, colorsArray, maxDisplayTiles):
        tileLine = {}
        tileLine['maxLength'] = maxDisplayTiles

        tiles = []
        
        for i in range(len(colorsArray)):
            for numColoredTiles in range(int(colorsArray[i])):
                tiles.append(self.getColorCssClass(i))
        
        while len(tiles) < maxDisplayTiles:
            tiles.append("")
                            
        return tiles

    def getFactories(self, boardState):
        factories = []
        for i in range(5):
            factories.append(self.getTileLine(boardState[i], 4))
        return factories
    
    def getCenter(self, boardState):
        return self.getTileLine(boardState[5], 100)

    def getBag(self, boardState):
        return boardState[6]
    
    def getLid(self, boardState):
        return boardState[7]
    
    def getPlayer(self, boardState, playerID):
        playerDict = {}

        if playerID == 1:
            startingRow = 8
        else:
            startingRow = 16
        
        playerDict['id'] = int(boardState[startingRow][0])
        playerDict['score'] = int(boardState[startingRow + 3][5])
        playerDict['bonusScore'] = int(boardState[startingRow + 4][5])
        
        playerLines = []
        for i in range(5):
            color = int(boardState[startingRow][i + 1])
            number = int(boardState[startingRow + 1][i + 1])
            tileCounts = [0, 0, 0, 0, 0, 0]
            tileCounts[color] = number
            playerLines.append(self.getTileLine(tileCounts, i + 1))

        playerDict['playerLines'] = playerLines

        playerDict['floorLine'] = self.getTileLine(boardState[startingRow + 2], 7)

        wall = []
        for i in range(5):
            wallRow = []
            for j in range(5):
                tile = {}
                tile['cssClass'] = self.getWallColorCssClass(i, j)
                tile['filled'] = int(boardState[startingRow + 3 + i][j])
                wallRow.append(tile)
            wall.append(wallRow)
        
        playerDict['wall'] = wall

        return playerDict

    def getBoardContextVars(self, boardState):
        retDict = {}

        retDict['board_state'] = boardState
        retDict['factories'] = self.getFactories(boardState)
        retDict['center'] = self.getCenter(boardState)
        retDict['bag'] = self.getBag(boardState)
        retDict['lid'] = self.getLid(boardState)
        retDict['player1'] = self.getPlayer(boardState, 1)
        retDict['player2'] = self.getPlayer(boardState, -1)
        
        return retDict
