from MCTS import MCTS
from azul.AzulGame import AzulGame
from azul.AzulPlayers import HumanAzulPlayer, RandomPlayer
from azul.pytorch.NNet import NNetWrapper as NNet
from azul.AzulArena import AzulArena

import cProfile, pstats, io
from pstats import SortKey

import numpy as np
from utils import *
import sqlite3
from datetime import datetime
"""
use this script to play any two agents against each other, or play manually with
any agent.
"""
g = AzulGame(shouldRandomize=False)

# all players
n1 = NNet(g)
n2 = NNet(g)

n1.load_checkpoint('./temp/', 'best.pth.tar')
n2.load_checkpoint('./temp/', 'best.pth.tar')
    
args = dotdict({'numMCTSSims': 50, 'cpuct': 1.0})
mcts = MCTS(g, n1, args)
mcts2 = MCTS(g, n2, args)
n1p = lambda x: np.argmax(mcts.getActionProb(x, temp=0))
n2p = lambda x: np.argmax(mcts2.getActionProb(x, temp=0))

player1 = n1p
player2 = n2p 

numberGames = 1
verbose = False

conn = sqlite3.connect("AzulGamesSite/AzulGameViewer/db.sqlite3")

for _ in range(numberGames):
    curTime = datetime.now().strftime("%m/%d/%y - %H:%M:%S")
    gameID = conn.cursor().execute('insert or replace into games_game(game_time) values (\"{0}\")'.format(curTime)).lastrowid
    arena = AzulArena(n1p, n2p, g, display=AzulGame.display, dbConn=(conn, gameID))
    arena.playFullGame(verbose=verbose)

conn.commit()


